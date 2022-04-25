from django import forms

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'title'
    }))
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'text'
    }))
    author = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'author'
    }))


