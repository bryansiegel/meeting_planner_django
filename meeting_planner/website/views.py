from datetime import datetime
from urllib import request

from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse('This page was served at' + str(datetime.now()))


def about(request):
    return HttpResponse('This is an About page')
