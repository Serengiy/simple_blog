from django import forms

from accounts.forms import User
from comments.models import Comment
from posts.models import Post


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput())
    # data = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = '__all__'
