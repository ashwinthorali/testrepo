from django.urls import path
from .views import signup_view, home, logout_view, signin_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('dashboard/', home, name='home'),
    path('', signin_view, name='signin'),
    path('logout/', logout_view, name='logout'),
]   
