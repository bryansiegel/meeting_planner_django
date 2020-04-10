from datetime import datetime
from urllib import request

from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return HttpResponse('Welcome To the Meeting Planner')


def date(request):
    return HttpResponse('This page was served at' + str(datetime.now()))


def about(request):
    return HttpResponse('This is an About page')
