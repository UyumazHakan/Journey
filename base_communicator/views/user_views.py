__author__ = 'Hakan Uyumaz'

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
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


def activate_view(request, activation_key):
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


def edit_profile_view(request):
    if request.user.is_authenticated():
        return render(request, 'edit_profile.html', {"user": request.user})
    else:
        return redirect("main")


def post_edit_profile(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            request.user.first_name = request.POST["name"]
            request.user.last_name = request.POST["surname"]
            request.user.email = request.POST["email"]
            if 'cover_photo' in request.FILES:
                request.user.cover_photo = request.FILES["cover_photo"]
            if 'profile_photo' in request.FILES:
                request.user.profile_photo = request.FILES["profile_photo"]
            request.user.save()
            return redirect("edit_profile")
        return redirect("main")
    return redirect("main")