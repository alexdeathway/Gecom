# Generated by Django 3.2.8 on 2022-01-21 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='default_profile_image.jpg', upload_to='profile_image'),
        ),
    ]