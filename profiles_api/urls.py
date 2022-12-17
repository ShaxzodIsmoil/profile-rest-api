from django.urls import path
from .views import HelloView


urlpatterns = [
    path('profile-api/', HelloView.as_view())
]