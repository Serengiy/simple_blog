from django.urls import path
from posts.views import PostDetailView, home_categories, add_post, PostUpdateView, PostDeleteView

urlpatterns = [
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('category/<int:pk>', home_categories, name='category'),
    path('add-post/', add_post, name='create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete')
]
