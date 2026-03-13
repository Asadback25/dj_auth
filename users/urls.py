from django.urls import path
from .views import update_profile , profile , change_password

urlpatterns = [
    path('update_profile/', update_profile, name='update_profile'),
    path('profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
]