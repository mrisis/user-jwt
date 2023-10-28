from django.urls import path
from .singup_api import SignupView
from .login_api import LoginView
from .user_list import UserListView

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='users'),
    ]
