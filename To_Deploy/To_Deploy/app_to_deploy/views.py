from django.http import HttpResponse
from django.shortcuts import render

from To_Deploy.app_to_deploy.models import KeyWord


def show_hello_world(request):
    context = {
        # 'message': KeyWord.objects.all()
        'message': 'Hello, World!'
    }
    return render(request, 'hello.html', context)
