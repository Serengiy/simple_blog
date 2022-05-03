from django.db import models
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.IntegerField(null=True)
    photo = models.ImageField(upload_to='static/images/', null=True, blank=True)
    address = models.CharField(max_length=300, null=True)

    def __str__(self):
        return str(self.user)


class EditUserForm(forms.ModelForm):
    photo = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    phone = forms.IntegerField(label='phone', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    address = forms.CharField(label='address', widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Profile
        fields = ('photo', 'address', 'phone',)


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя юзера'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Такого юзера нет в системе')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Данный пользователь не активен')
            return super().clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя юзера'
    }))

    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите email'
    }))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']
