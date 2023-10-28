from django.urls import path, include


app_name = 'accounts'
urlpatterns = [
    path('api/v1/accounts/', include('accounts.api.v1.urls', namespace='v1')),
    ]
