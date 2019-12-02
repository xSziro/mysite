from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.


def index(request):
    all = User.object.all()
    return HttpResponse("Pierwsza apk django")
    

def test(request):
    p = User(name = 'user1',password = 'abcd1234', email = 'www2www@w.ww')
    p.save()
    return HttpResponse("test")

