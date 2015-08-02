__author__ = 'Hakan Uyumaz'

from django.shortcuts import render, redirect

from base_communicator.models import Journey


def main_page_view(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        return render(request, "main.html")


def home_page_view(request):
    if request.user.is_authenticated():
        return render(request, "home.html",
                      {"user": request.user, "journeys": Journey.objects.filter(owner=request.user)})
    else:
        return redirect('main')