from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from task.views2 import TaskViewSet, api_root
from task import views, views2
from rest_framework import renderers


# API endpoints
router = DefaultRouter()
router.register(r'tasks', views2.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


