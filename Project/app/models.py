from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.hashers import make_password, check_password
from picklefield.fields import PickledObjectField
# Create your models here.

class ApiUser(AbstractUser):
    username = models.CharField(max_length=255, null=False, blank=False, primary_key=True)
    password = models.CharField(max_length=1000, null=False, blank=False)

    USERNAME_FIELD = "username"

    def make_password_hash(self, raw_password:str) -> str:
        hashed_password = make_password(raw_password)
        return hashed_password

    def validate_password(self, raw_password: str) -> bool:
        return check_password(raw_password)

class File(models.Model):
    uploaded_by = models.ForeignKey(ApiUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True)
    content = PickledObjectField()
    upload_date = models.DateTimeField(auto_now_add=True)