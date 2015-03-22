__author__ = 'Hakan Uyumaz'


import http.client

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from ..models import Note,Journey
from ..forms import JourneyCreationForm, NoteCreationForm

def create_journey(request):
    if request.user.is_authenticated():
        if request.method == "POST" :
            form = JourneyCreationForm(request.POST)
            if not form.errors:
                journey = form.save(False)
                journey.owner = request.user
                if request.POST["summary"] :
                    journey.summary = request.POST["summary"]
                journey.save()
    return redirect('main')

def add_note(request, journey_id):
    if request.user.is_authenticated():
        journey = get_object_or_404(Journey, pk=journey_id)
        if request.method == "POST":
            form = NoteCreationForm(request.POST)
            if not form.errors and journey:
                note = form.save(False)
                note.journey = journey
                note.save()
            return redirect('journey', journey_id)
        else:
            return render(request, "note_add.html", {"journey": journey})

def journey_view(request, journey_id):
    if request.user.is_authenticated():
        journey = get_object_or_404(Journey, pk= journey_id)
        return render(request, "journey.html", {"journey" : journey})

def new_journey_view(request):
    if request.user.is_authenticated():
        return render(request, "journey_creator.html")
    else:
        redirect('main')
