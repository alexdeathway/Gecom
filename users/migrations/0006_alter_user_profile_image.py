# Generated by Django 3.2.16 on 2023-04-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_discription_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='profile_image/default_profile_image.jpg', upload_to='profile_image'),
        ),
    ]
