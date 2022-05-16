# Generated by Django 4.0.4 on 2022-05-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_photo_post_image_alter_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='is published'),
        ),
    ]
