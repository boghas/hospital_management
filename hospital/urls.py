from django.urls import path
from .views import About, Home, Contact, Login, Logout_admin

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='admin_login'),
    path('admin_logout/', Logout_admin, name='admin_logout'),
]
