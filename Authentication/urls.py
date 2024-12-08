from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard.as_view(),name='dashboard'),
    path('signin/', signin.as_view(), name='signin'),
    path('signup/', signup.as_view(),name='signup'),
    path('logout/', signout.as_view(),name='logout'),
    path('profile/', profile.as_view(),name='profile'),
    path('edit-profile/', edit_profile.as_view(),name='edit_profile'),
]
