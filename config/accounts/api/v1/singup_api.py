from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
import jwt


class SignupView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        fullname = request.data['fullname']
        phone = request.data['phone']
        hashed_password = make_password(password)
        user = User.objects.create(username=username, password=hashed_password, fullname=fullname, phone=phone)
        return Response({"message": "User Created Successfully."})
