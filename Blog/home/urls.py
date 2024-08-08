from django.urls import path
from .views import BlogAPiView,PublicApiView
urlpatterns = [
    path('blogs/',BlogAPiView.as_view(),name='blogs'),
    path('public-blogs/',PublicApiView.as_view(),name='public-blogs'),
]
