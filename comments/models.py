from django.db import models
from accounts.forms import User
from posts.models import Post


class Comment(models.Model):
    text = models.CharField(max_length=500, verbose_name='Комментарий')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, )

    class Meta:
        ordering = ['date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.author, self.text)