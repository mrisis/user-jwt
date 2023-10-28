from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User


class UserListView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            users = User.objects.all()
            user_list = [{"username": user.username, "fullname": user.fullname, "phone": user.phone} for user in users]
            return Response({"users": user_list})
        else:
            return Response({"error": "You must be logged in to view the user list."})

