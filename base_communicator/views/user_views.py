__author__ = 'Hakan Uyumaz'

import http.client

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from ..forms import UserCreationForm

from base_communicator.models import User

from ..utils import generate_token, send_activation_mail

def register_view(request):
    if request.user.is_authenticated():
        return redirect("homepage")
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.errors:
                print(form.errors)
                return redirect('main')

            user = form.save()
            print(str(user) + " successfully registered")
            send_activation_mail(user)
            print(str(user) + "'s activation mail has sent")

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

def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect("main")

def activate_view(request,activation_key):
    try:
        user = User.objects.get(activation_key=activation_key)
    except User.DoesNotExist:
        return redirect("main")

    if not user.is_active:
        if user.activation_expire_date < timezone.now():
            user.activation_key = generate_token()
            user.save()
            send_activation_mail(user)
            return redirect("main")

        user.is_active = True
        user.save()

        return redirect("main")
    else:
        return redirect("main")
