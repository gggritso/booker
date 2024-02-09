from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("by_author/", views.by_author, name="by_author"),
]
