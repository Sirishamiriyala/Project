from django.urls import path

from . import views
from django.conf import Settings

urlpatterns = [

    path('getTest/',views.getAPI)
]

