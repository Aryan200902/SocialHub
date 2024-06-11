from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle
from djoser.views import TokenCreateView, TokenDestroyView

class CustomTokenCreateView(TokenCreateView):
    def _action(self, serializer):
        user = serializer.validated_data['user']
        token = self.token_model.objects.create(user=user)
        return Response(
            {
                'token': token.key,
                'message': 'Successfully logged in.'
            },
            status=status.HTTP_200_OK
        )

class CustomTokenDestroyView(TokenDestroyView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_204_NO_CONTENT)
       
class CustomPagination(PageNumberPagination):
    page_size = 10

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return CustomUser.objects.filter(
            Q(email__iexact=query) | Q(username__icontains=query)
        )

class FriendRequestThrottle(UserRateThrottle):
    rate = '3/min'

class SendFriendRequestView(APIView):
    throttle_classes = [FriendRequestThrottle]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        # Implementation of sending friend request logic
        pass

class AcceptFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, request_id):
        # Implementation of accepting friend request logic
        pass

class RejectFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, request_id):
        # Implementation of rejecting friend request logic
        pass

class ListFriendsView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Implementation of listing friends logic
        pass

class PendingFriendRequestsView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Implementation of listing pending friend requests logic
        pass
