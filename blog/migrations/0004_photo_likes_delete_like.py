# Generated by Django 4.2.5 on 2023-09-13 08:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0003_remove_photo_likes_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="likes",
            field=models.ManyToManyField(
                related_name="liked_photos", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(name="Like",),
    ]
