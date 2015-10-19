__author__ = 'Hakan Uyumaz'

from django.shortcuts import render, redirect
from django.db.models import Q

from base_communicator.models import Friendship, User


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
        journeys = user.owned_journeys.all()
        return render(request, "home.html",
                      {"user": request.user, "journeys": journeys})
    else:
        return redirect('main')


def search_page_view(request):
    key = request.GET["key"]
    if request.user.is_authenticated():
        users = User.objects.filter(Q(name=key) | Q(surname=key))
        return render(request, "search.html", {"users": users})
    else:
        return redirect('main')


def newsfeed_page_view(request):
    if request.user.is_authenticated():
        try:
            followings = Friendship.objects.get(owner=request.user)
        except Friendship.DoesNotExist:
            followings = []
        journeys = []
        for following in followings:
            journeys.append(following.owned_journeys.all())
        return render(request, "journeys.html", {"user": request.user, "journeys": journeys})
    else:
        return redirect('main')