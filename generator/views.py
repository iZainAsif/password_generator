from django.shortcuts import render
import random
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def zain(request):
    return render(request,'generator/about.html')

def password(request):
    characs=list('abcdefghijklmnopqrstuvwxyz')
    thepass=''
    len=int(request.GET.get('Lenght',10))
    if request.GET.get('uppercase'):
        characs.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Numbers'):
        characs.extend(list('1234567890'))

    if request.GET.get('Special'):
        characs.extend(list('!@#$%^&*'))

    for i in range(len):
        thepass+=random.choice(characs)
    return render(request,'generator/password.html',{'password':thepass})