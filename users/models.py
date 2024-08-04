from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLES=(
        ("Admin","Admin"),
        ("Manager", "Manager"),
        ("Student", "Student"),
    )
    user_role = models.CharField(default='Student',choices=ROLES,max_length=100)