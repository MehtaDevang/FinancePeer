from django.urls import path

from . import views

urlpatterns = [
    path('user/$', views.User.as_view(), name='user'),
    path('login/$', views.Login.as_view(), name="login"),
    path('validate/$', views.Validator.as_view(), name='validator'),
    path('getFiles/$', views.Files.as_view(), name="get_files"),
    path('getFileData/$', views.FileDetails.as_view(), name="file_data"),
]