from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("by_id/", views.by_id, name="by_id"),
    path("by_author/", views.by_author, name="by_author"),
]
