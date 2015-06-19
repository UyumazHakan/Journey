__author__ = 'Hakan Uyumaz'

import http.client

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from base_communicator.models import User, Friendship, FriendshipRequest

def add_friend(request):
    if request.user.is_authenticated():
        if request.method == "POST" :
            friendship_request = FriendshipRequest()
            friendship_request.sender = request.user
            try:
                friend = User.objects.get(public_id=request.POST["friend"])
            except User.DoesNotExist:
                return redirect("main")
            friendship_request.receiver = friend
            friendship_request.status = 'P'
            friendship_request.save()
    return redirect('main')