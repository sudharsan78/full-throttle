from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class User(AbstractUser):
	user_id = models.CharField(max_length=9, validators=[MinLengthValidator(9)], blank=True)
	time_zone = models.CharField(max_length=50, blank=True)


class UserActivity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	start_time = models.DateTimeField(blank=True)
	end_time = models.DateTimeField(blank=True, null=True)
