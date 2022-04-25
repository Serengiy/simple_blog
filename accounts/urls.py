from django.urls import path
from accounts.views import registration_view, login_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registration_view, name='register')
]