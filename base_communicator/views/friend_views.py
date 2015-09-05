__author__ = 'Hakan Uyumaz'

from django.shortcuts import redirect, render

from base_communicator.models import User, FriendshipRequest, Friendship


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


def follower_page_view(request, user_id):
    if request.user.is_authenticated():
        try:
            user = User.objects.get(public_id=user_id)
        except User.DoesNotExist:
            return redirect("main")
        try:
            follower = Friendship.objects.get(owner=user)
        except Friendship.DoesNotExist:
            follower = []
        return render(request, 'friends_list.html', {"users": follower})
    else:
        return redirect('main')


def following_page_view(request, user_id):
    if request.user.is_authenticated():
        try:
            user = User.objects.get(public_id=user_id)
        except User.DoesNotExist:
            return redirect("main")
        try:
            following = Friendship.objects.get(owner=user)
        except Friendship.DoesNotExist:
            following = []

        return render(request, 'friends_list.html', {"users": following})
    else:
        return redirect('main')