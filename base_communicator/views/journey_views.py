__author__ = 'Hakan Uyumaz'


import http.client

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

def create_journey(request):
    if request.user.is_authenticated():
        if request.method == "POST" :
            return None
