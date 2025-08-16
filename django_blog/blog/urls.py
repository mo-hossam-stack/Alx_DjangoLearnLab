from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register_view,profile_view,home_view

urlpatterns = [
    path('', home_view, name='home'),
path('login/', CustomLoginView.as_view(), name='login'),
path('logout/', CustomLogoutView.as_view(), name='logout'),
path('register/', register_view, name='register'),
path('profile/', profile_view, name='profile'),
]