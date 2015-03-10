__author__ = 'Hakan Uyumaz'

import http.client

from django.shortcuts import render, redirect
from django.http import HttpResponse

from base_communicator.models import user

def main_page_view(request):
    return render(request, "main.html")