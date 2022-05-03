from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from accounts.forms import User
from comments.forms import CommentForm
from comments.models import Comment
from posts.forms import PostForm
from posts.models import Post


class HomeListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    paginate_by = 10


def home_categories(request, pk):
    paginator = Paginator(Post.objects.all().filter(category=str(pk)), 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'posts/home.html', {'page_obj': posts})


class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'posts/update.html'
    success_message = 'Пост успешно обновлен'
    fields = ['text', 'category']

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})


class PostDeleteView(DeleteView):
    model = Post
    success_message = 'Пост успешно удален'

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})


def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        messages.success(request, 'Пост создан')
        author = User.objects.filter(id__in=str(request.POST['author'])).first()
        form = PostForm(request.POST, initial={'author': author})
        if form.is_valid():
            form.save()
            return redirect('profile', username=author.username)
        return render(request, 'posts/create.html', {'form': form})
    return render(request, 'posts/create.html', {'form': form})


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.kwargs['pk'])
        context['form'] = CommentForm
        return context
