__author__ = 'Hakan Uyumaz'

from django.shortcuts import render, redirect

from ..models import Journey, JourneyElement, Note, Photo, Comment


def create_journey(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            request_body = request.POST
            journey = Journey()
            if 'photo' in request.FILES:
                journey.photo = request.FILES['photo']
            journey.title = request_body["title"]
            journey.position = request_body["position"]
            journey.category = request_body["category"]
            journey.summary = request_body["summary"]
            journey.owner = request.user
            journey.last_element_index = 0
            journey.save()
            journey.users.add(request.user)
            print("OK")
    print("NK")
    return redirect('main')


def add_note(request, journey_id):
    if request.user.is_authenticated():
        print("OKKK")
        if request.method == "POST":
            request_body = request.POST
            try:
                journey = Journey.objects.get(pk=journey_id)
                print(str(journey))
            except Journey.DoesNotExist:
                return redirect("main")
            note = Note()
            note.title = request_body['title']
            note.text = request_body['text']
            note.save()
            journey_element = JourneyElement()
            journey_element.type = 'N'
            journey_element.note = note
            journey_element.index = journey.last_element_index + 1
            journey_element.journey = journey
            journey.last_element_index = journey.last_element_index + 1
            journey_element.save()
            journey.save()
    return redirect('main')


def add_image(request, journey_id):
    if request.user.is_authenticated():
        if request.method == "POST":
            request_body = request.POST
            try:
                journey = Journey.objects.get(pk=journey_id)
                print(str(journey))
            except Journey.DoesNotExist:
                return redirect("main")
            image = Photo()
            image.title = request_body['title']
            image.photo = request.FILES['image']
            image.save()
            journey_element = JourneyElement()
            journey_element.type = 'P'
            journey_element.photo = image
            journey_element.index = journey.last_element_index + 1
            journey_element.journey = journey
            journey.last_element_index = journey.last_element_index + 1
            journey_element.save()
            journey.save()
    return redirect('main')


def create_note(request, journey_id):
    if request.user.is_authenticated():
        try:
            journey = Journey.objects.get(pk=journey_id)
        except Journey.DoesNotExist:
            return redirect("main")
        return render(request, "note_creator.html", {"journey": journey})


def create_image(request, journey_id):
    if request.user.is_authenticated():
        try:
            journey = Journey.objects.get(pk=journey_id)
        except Journey.DoesNotExist:
            return redirect("main")
        return render(request, "image_creator.html", {"journey": journey})


def add_comment(request, journey_id):
    if request.user.is_authenticated():
        if request.method == "POST":
            request_body = request.POST
            try:
                journey = Journey.objects.get(pk=journey_id)
                print(str(journey))
            except Journey.DoesNotExist:
                return redirect("main")
            comment = Comment()
            comment.text = request.POST["text"]
            comment.user = request.user
            comment.journey = journey
            comment.save()
    return redirect('main')


def create_comment(request, journey_id):
    if request.user.is_authenticated():
        try:
            journey = Journey.objects.get(pk=journey_id)
        except Journey.DoesNotExist:
            return redirect("main")
        return render(request, "comment_creator.html", {"journey": journey})


def journey_view(request, journey_id):
    if request.user.is_authenticated():
        try:
            journey = Journey.objects.get(pk=journey_id)
        except Journey.DoesNotExist:
            return redirect("main")
        return render(request, "journey.html", {"journey": journey})


def new_journey_view(request):
    if request.user.is_authenticated():
        return render(request, "journey_creator.html")
    else:
        redirect('main')


def accessible_journeys(request):
    if request.user.is_authenticated():
        journeys = request.user.journeys.all()
        return render(request, "journeys.html", {"user": request.user, "journeys": journeys})
    else:
        redirect('main')


def love_journey(request, journey_id):
    if request.user.is_authenticated():
        try:
            journey = Journey.objects.get(pk=journey_id)
        except Journey.DoesNotExist:
            return redirect("main")
        request.user.love_journey(journey)
        return redirect('main')


def share_journey(request, journey_id):
    if request.user.is_authenticated():
        try:
            journey = Journey.objects.get(pk=journey_id)
        except Journey.DoesNotExist:
            return redirect("main")
        request.user.share_journey(journey)
        return redirect('main')