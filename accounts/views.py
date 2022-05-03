from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from accounts.forms import UserRegistrationForm, UserLoginForm, User, EditUserForm, Profile
from posts.models import Post


def author_page(request, username):
    user = User.objects.filter(username=username).first()
    posts = Post.objects.filter(author=user.pk).all()
    paginator = Paginator(posts, 3)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'profile.html', {'username': user, 'page_obj': page_obj})


def logout_view(request):
    logout(request)
    return redirect('/')


class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    form_class = EditUserForm
    success_message = 'Профиль обновлен успешно!'

    def post(self, request, *args, **kwargs):
        context = super(ProfileUpdateView, self).post(self, request, *args, **kwargs)
        self.object.user.first_name = self.request.POST['first_name']
        self.object.user.last_name = self.request.POST['last_name']
        self.object.user.save()
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile', kwargs={'username': self.object.user.username})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    _next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        _next = _next or '/'
        return redirect(_next)
    return render(request, 'accounts/login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/register_done.html')
        return render(request, 'accounts/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
