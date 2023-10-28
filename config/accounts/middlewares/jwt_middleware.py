import jwt
from django.http import JsonResponse
from accounts.models import User

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authorization_header = request.headers.get('Authorization')
        if authorization_header:
            token = authorization_header.split(' ')[1]
            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user = User.objects.get(id=payload['id'])
                request.user = user
            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'Token expired'}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'error': 'Invalid token'}, status=401)
        response = self.get_response(request)
        return response
