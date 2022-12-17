from django.urls import path, include
from .views import HelloView, HelloViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello', HelloViewSet, basename='hello-viewset')


urlpatterns = [
    path('profile-api/', HelloView.as_view()),
    path('', include(router.urls))
]