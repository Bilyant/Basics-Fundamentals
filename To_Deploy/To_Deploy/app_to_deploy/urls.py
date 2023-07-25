from django.urls import path

from To_Deploy.app_to_deploy.views import show_hello_world

urlpatterns = (
    path('', show_hello_world, name='hello world'),
)
