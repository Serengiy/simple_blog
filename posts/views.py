from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from comments.forms import CommentForm
from comments.models import Comment
from posts.models import Post, Category


def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

def home_categories(request, pk):
    posts = Post.objects.all().filter(category=str(pk))
    return render(request, 'posts/home.html', {'posts': posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.kwargs['pk'])
        context['form'] = CommentForm
        return context







