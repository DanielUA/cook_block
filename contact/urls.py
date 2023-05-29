from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("feedback/", views.CreateContact.as_view(), name="feedback"),
]
