import importlib
import logging
import os
import queue
import re
import time
from enum import Enum
from threading import Thread, Event
from typing import List, Optional

from programs.programs.program_plugin import ProgramPlugin
from utils.exceptions import IllegalStateException

logger = logging.getLogger(__name__)


class State(Enum):
    NO_PROGRAM = 0
    PROGRAM_RUNNING = 1


class ProgramManager:

    var_queue = queue.Queue()
    stop_program_flag: Event = Event()
    active_program: Optional[ProgramPlugin] = None
    program_thread: Optional[Thread] = None

    @staticmethod
    def load_programs():
        logger.debug("Loading plugin programs")

        files = os.listdir('programs/plugins')
        test = re.compile(".py$", re.IGNORECASE)
        files = filter(test.search, files)
        module_names = ['.' + os.path.splitext(f)[0] for f in files]

        for mod in module_names:
            importlib.import_module(mod, package='programs.plugins')

        for plugin in ProgramPlugin.plugins:
            logger.debug("Loaded plugin {}".format(plugin))

    @staticmethod
    def get_program_list() -> List[str]:
        return [p.__name__ for p in ProgramPlugin.plugins]

    @staticmethod
    def start_program(program_name: str):
        logger.debug(f"Starting program {program_name}")

        if ProgramManager.is_program_active():
            logger.error("Tyring to start a program but there is still a program running")
            return

        for plugin in ProgramPlugin.plugins:
            if plugin.__name__ == program_name:
                ProgramManager.active_program = plugin()
                ProgramManager.program_thread = Thread(target=ProgramManager.program_loop)
                ProgramManager.program_thread.start()
                break
            else:
                continue

    @staticmethod
    def stop_program():
        if not ProgramManager.is_program_active():
            logger.error("Trying to stop a program but no program is running")
            return

        ProgramManager.stop_program_flag.set()
        ProgramManager.program_thread.join()
        ProgramManager.active_program = None
        ProgramManager.program_thread = None
        ProgramManager.stop_program_flag.clear()

    @staticmethod
    def set_variables(variables):
        if ProgramManager.is_program_active():
            ProgramManager.var_queue.put(variables)

    @staticmethod
    def program_loop():
        ProgramManager.active_program.on_start()

        program_start = time.time_ns()
        update_start = time.time_ns()

        while not ProgramManager.stop_program_flag.is_set():
            now = time.time_ns()
            seconds_since_last_update = (now - update_start) * 1e-9
            seconds_since_start = (now - program_start) * 1e-9

            update_start = now
            try:
                while True:
                    var = ProgramManager.var_queue.get(block=False)
                    ProgramManager.active_program.set_variables(var)
            except queue.Empty:
                pass

            ProgramManager.active_program.update(seconds_since_start, seconds_since_last_update)
            update_end = time.time_ns()

            # 60 Hz target speed
            # Sleep if the program was quicker than 60 Hz.
            sleep = 0.0166666 - ((update_end - update_start) * 1e-9)
            if sleep > 0:
                time.sleep(sleep)

        ProgramManager.active_program.on_stop()

    @staticmethod
    def is_program_active() -> bool:
        if ProgramManager.active_program is None and ProgramManager.program_thread is None:
            return False
        elif ProgramManager.active_program is not None and ProgramManager.program_thread is not None:
            return True
        else:
            raise IllegalStateException("active_program and program_thread not in sync")


ProgramManager.load_programs()
