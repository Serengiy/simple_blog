from django.contrib import admin
from django.urls import path
from posts.views import PostDetailView, home_categories

urlpatterns = [
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('category/<int:pk>', home_categories, name='category')
    # path('all_categories/', all_categories, name = 'all_categories')
]
