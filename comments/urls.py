from comments.views import CommentDeleteView, CommentUpdateView, add_comment
from posts.views import *
from django.urls import path

app_name = 'comments'

urlpatterns = [
    path('delete/<int:pk>/<int:p_pk>', CommentDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/<int:p_pk>', CommentUpdateView.as_view(), name='update'),
    path('add/<int:pk>', add_comment, name='add')
]