__author__ = 'Hakan Uyumaz'

import http.client

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..forms import JourneyUserCreationForm

from base_communicator.models import user

def register_view(request):
    if request.user.is_authenticated():
        return redirect("homepage")
    else:
        if request.method == "POST":
            form = JourneyUserCreationForm(request.POST)
            if form.errors:
                print(form.errors)
                return redirect('main')

            user = form.save()
            print(str(user) + " successfully registered")

        return redirect("main")

def login_view(request):
    if request.user.is_authenticated():
        redirect("main")
    else:
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if email and password:
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
        return redirect("main")
