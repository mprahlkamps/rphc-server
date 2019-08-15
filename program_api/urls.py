from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListPrograms.as_view()),
    path('start/', views.StartProgram.as_view()),
    path('stop/', views.StopProgram.as_view()),
    path('restart/', views.RestartProgram.as_view()),
    path('set-variables/', views.SetProgramVariables.as_view()),
]
