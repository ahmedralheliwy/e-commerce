from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns=[
    path('register/',views.register_view, name='register'),
    path('dashboard/',views.dashboard_view, name='dashboard'),
    path('logout/',views.logout_view, name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
]