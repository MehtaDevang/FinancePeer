from msilib.schema import File
from django.contrib import admin

from app.models import ApiUser, File

# Register your models here.
admin.site.register(ApiUser)
admin.site.register(File)