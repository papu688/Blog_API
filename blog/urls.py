from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BlogView


router = DefaultRouter()
router.register(r'blog', BlogView)

urlpatterns = [
    path('', include(router.urls)),
]