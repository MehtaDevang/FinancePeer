# Generated by Django 3.2.15 on 2022-08-09 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220809_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('content', picklefield.fields.PickledObjectField(editable=False)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
