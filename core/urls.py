from django.urls import path
from .views import *

urlpatterns = [
    path('auth/token/login/', CustomTokenCreateView.as_view(), name='login'),
    path('auth/token/logout/', CustomTokenDestroyView.as_view(), name='logout'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend-request/send/<int:user_id>/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('friend-request/accept/<int:request_id>/', AcceptFriendRequestView.as_view(), name='accept-friend-request'),
    path('friend-request/reject/<int:request_id>/', RejectFriendRequestView.as_view(), name='reject-friend-request'),
    path('friends/', ListFriendsView.as_view(), name='list-friends'),
    path('friend-requests/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
]
