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
            friendships = Friendship.objects.filter(friend=user).all()
        except Friendship.DoesNotExist:
            friendships = []
        followers = []
        for friendship in friendships:
            followers.append(friendship.owner)
        return render(request, 'friends_list.html', {"users": followers})
    else:
        return redirect('main')


def following_page_view(request, user_id):
    if request.user.is_authenticated():
        try:
            user = User.objects.get(public_id=user_id)
        except User.DoesNotExist:
            return redirect("main")
        try:
            friendships = Friendship.objects.filter(owner=user).all()
        except Friendship.DoesNotExist:
            friendships = []
        followings = []
        for friendship in friendships:
            followings.append(friendship.friend)
        return render(request, 'friends_list.html', {"users": followings})
    else:
        return redirect('main')


def requests_page_view(request):
    if request.user.is_authenticated():
        try:
            friendship_requests = FriendshipRequest.objects.get(receiver=request.user)
        except FriendshipRequest.DoesNotExist:
            friendship_requests = []
        return render(request, 'request_list.html', {"friendship_requests": friendship_requests})
    else:
        return redirect('main')


def follow(request, user_id):
    if request.user.is_authenticated():
        try:
            friend = User.objects.get(public_id=user_id)
        except User.DoesNotExist:
            return redirect('main')
        friendship = Friendship()
        friendship.type = 'Fo'
        friendship.owner = request.user
        friendship.friend = friend
        friendship.save()
        return redirect('main')
    else:
        return redirect('main')