from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def validate(request):
    return JsonResponse({
        'name': 'Jair',
        'job': 'developer'
    })
