from django.urls import path
from .views import index

urlpatterns = [
    path('<slug:slug>', index),
    path('<slug:slug>/<str:roomCode>', index),
]
