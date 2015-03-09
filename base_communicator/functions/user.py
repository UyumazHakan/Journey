__author__ = 'Hakan Uyumaz'

import json

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse

from ..forms import JourneyUserCreationForm

RESPONSE_JSON = {}

def register(request):
    if request.method == "POST":
        form = JourneyUserCreationForm(request.POST)
        if form.errors:
            RESPONSE_JSON["status"] = 1
            RESPONSE_JSON["description"] = "Form Error Occurred"
            RESPONSE_JSON["error"] = form.errors
            return HttpResponse(json.dumps(RESPONSE_JSON))
        form.save()
        RESPONSE_JSON["status"] = 0
        RESPONSE_JSON["description"] = "User created"
        return HttpResponse(json.dumps(RESPONSE_JSON))
    else:
        RESPONSE_JSON["status"] = 1
        RESPONSE_JSON["description"] = "No POST request found"
        return HttpResponse(json.dumps(RESPONSE_JSON))

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
                login(request, user)
                RESPONSE_JSON["status"] = 0
                RESPONSE_JSON["container"] = {}
                RESPONSE_JSON["container"]["username"] = user.username
                RESPONSE_JSON["container"]["name"] = user.name
                RESPONSE_JSON["container"]["surname"] = user.surname
                RESPONSE_JSON["container"]["email"] = user.email
                RESPONSE_JSON["message"] = "Authenticated user cannot register"
                return HttpResponse(json.dumps(RESPONSE_JSON))
        else:
            RESPONSE_JSON["status"] = 1
            RESPONSE_JSON["message"] = "User credentials are not correct."
            return HttpResponse(json.dumps(RESPONSE_JSON))
    else:
        RESPONSE_JSON["status"] = 1
        RESPONSE_JSON["message"] = "No request found."
        return HttpResponse(json.dumps(RESPONSE_JSON))