__author__ = 'Hakan Uyumaz'

from django.shortcuts import redirect

from base_communicator.models import User, FriendshipRequest


def add_friend(request):
    if request.user.is_authenticated():
        if request.method == "POST":
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