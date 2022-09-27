from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(blank=False, max_length=100)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='ads_images/', null=True)


class Comment(models.Model):
    text = models.TextField(max_length=3500)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE
    )
