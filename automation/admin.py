from django.contrib import admin

from automation.models import Action, Scene, SetLedStripColorAction, EnableRemoteSocketAction, DisableRemoteSocketAction

admin.site.register(Action)
admin.site.register(Scene)
admin.site.register(EnableRemoteSocketAction)
admin.site.register(DisableRemoteSocketAction)
admin.site.register(SetLedStripColorAction)
