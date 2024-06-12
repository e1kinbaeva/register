from django.urls import path
from apps.user.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("",index , name="index"),
    path('register/',register, name="register"),
    path('profile/<int:id>/', profile, name="profile"),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout")
]