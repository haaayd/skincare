from django.shortcuts import render

from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
def about(request):
    return HttpResponse('<h1>About the Profile-user</h1>')