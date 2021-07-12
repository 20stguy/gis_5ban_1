from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')
        # temp에서 받은걸 new_hello_world에 넣어준다
        new_hello_world = HelloWorld()
        # model에 넣어준다
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reversed('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})