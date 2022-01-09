from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='teambuilding/account/login.html'), name='login'),
    path('activate/<uid_64>/<token>/', views.activate, name='activate'),
]
