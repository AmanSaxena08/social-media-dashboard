from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter_handle = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# Create your models here.
