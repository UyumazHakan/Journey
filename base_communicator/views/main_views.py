__author__ = 'Hakan Uyumaz'

from django.shortcuts import render, redirect
from django.db.models import Q

from base_communicator.models import Journey, Friendship


def main_page_view(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        return render(request, "main.html")


def home_page_view(request):
    if request.user.is_authenticated():
        user = request.user
        user.followers = Friendship.objects.filter(friend=user, type='Fo')
        user.followings = Friendship.objects.filter(owner=user, type='Fo')
        user.friends = Friendship.objects.filter((Q(owner=user) | Q(friend=user)) & Q(type='Fr'))
        user.journeys = Journey.objects.filter(owner=request.user)
        print(str(user.educations.all()))
        return render(request, "home.html",
                      {"user": request.user})
    else:
        return redirect('main')