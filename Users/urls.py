from django.contrib.auth.views import LogoutView
from django.urls import path

from Users.views import UsersView, RegisterView, LoginView, CiudadesView

urlpatterns = [
    path('todos-usuarios/',UsersView.as_view()),
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('citis/',CiudadesView.as_view()),

]