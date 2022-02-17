from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', max_length=100, null=True, blank=True, verbose_name='Изображение')
    description = models.TextField()
    views = models.IntegerField(default=0)
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'