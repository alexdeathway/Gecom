# Generated by Django 3.2.8 on 2021-10-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_gamesmodel_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='cover',
            field=models.ImageField(default='default_category_cover.jpg', upload_to='category_cover'),
        ),
    ]