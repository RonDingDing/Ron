from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Texte
import json
# Create your views here.

from django import forms
from django.forms.models import model_to_dict


def index(request):
    return render(request, 'polls/entry.html', {})


def choose(request):

    if request.method == 'POST':
        Texte.objects.all().delete()
        string = request.POST.get('apple')
        if string:
            namelist = [i for i in string.replace("\r", "").split("\n") if i]
            result = random.choice(namelist)
            namelist.remove(result)
            namelist = set(namelist)
            for i in namelist:
                Texte.objects.create(text=str(i))

        return render(request, 'polls/result.html', {'result': result})
    elif request.method == 'GET':
        a = Texte.objects.count()
        if a == 0:
            result = "没有可用的抽奖者了"
        else:
            index = random.randint(0, a - 1)
            result = Texte.objects.all()[index]
            result.delete()
        return render(request, 'polls/result.html', {'result': result})
