from django.urls import path
from .views import BlogAPiView
urlpatterns = [
    path('blog/',BlogAPiView.as_view(),name='blog'),
]
