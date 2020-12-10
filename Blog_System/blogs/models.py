from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Blog(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
