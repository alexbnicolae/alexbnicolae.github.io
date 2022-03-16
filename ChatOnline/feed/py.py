my_friends = FriendList.objects.none()
    room_chat = Room.objects.none()
    if request.user.is_authenticated:
        my_friends = FriendList.objects.filter(user1 = request.user)

        for mf in my_friends:
            if FriendList.objects.filter(user1 = mf.user2, user2 = request.user).exists():
                mf2 = FriendList.objects.get(user1 = mf.user2, user2 = request.user)
                if Room.objects.filter(friendship1 = mf, friendship2 = mf2).exists() == False:
                   room_chat = Room.objects.create(friendship1 = mf, friendship2 = mf2)

        