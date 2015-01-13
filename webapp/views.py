from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth


def index(request):
    return render(request, 'index.html', {'user': request.user})

@login_required
def protected(request):
    return render(request, 'protected.html', {'user': request.user})

def logout(request):
    auth.logout(request)
    return HttpResponse("")
