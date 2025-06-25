from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True ,blank=True)  # ✅ Links to auth_user
    email = models.EmailField(unique=True, default="default@example.com")
    firstname = models.CharField(max_length=25, default="not registered")
    lastname = models.CharField(max_length=20, default="not registered")
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
