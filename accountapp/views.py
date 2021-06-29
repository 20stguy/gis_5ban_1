from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    return HttpResponse('Hello World!') # 철자만 정확하게 외우고 있으면 불러오는건 Pycharm이 해준다

