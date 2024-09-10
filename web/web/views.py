"""
View page
"""
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hello_world(request):
    mgs = {"mgs": "hi everyone"}
    return JsonResponse(mgs)
