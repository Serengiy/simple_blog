from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, UpdateView
from comments.forms import CommentForm
from comments.models import Comment


def add_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('posts:detail', kwargs={'pk': pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('posts:detail', kwargs={'pk': self.kwargs.get('p_pk')})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['text']
    success_url = reverse_lazy('post:detail')

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('posts:detail', kwargs={'pk': self.kwargs.get('p_pk')})
