from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=3000)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['date']
