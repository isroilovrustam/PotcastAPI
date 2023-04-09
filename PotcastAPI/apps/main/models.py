from django.db import models
from apps.profil.models import Profile


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
