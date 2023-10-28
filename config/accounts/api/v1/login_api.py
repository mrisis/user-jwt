from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User, OTP
import jwt


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        otp = request.data['otp']
        user = User.objects.get(username=username)
        user_otp = OTP.objects.filter(user=user).order_by('-timestamp').first()
        if user and check_password(password, user.password) and user_otp and user_otp.otp == otp:
            payload = {
                'id': user.id,
                'username': user.username,
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')
            return Response({"token": token, 'message': 'Login successfully'})
        else:
            return Response({"error": "Invalid username or password or otp"})
