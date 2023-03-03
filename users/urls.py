from django.urls import path
from . import views

urlpatterns = [
    #path('user/register/', views.register_user, name="user-register"),

    path('user/register/', views.RegisterUserAPIView.as_view(), name="user-register"),
    path('user/login/', views.LoginUserApiView.as_view(), name="user-login"),
]
