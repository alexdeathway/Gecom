# Generated by Django 3.2.8 on 2021-10-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20211010_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishermodel',
            name='email',
            field=models.EmailField(blank=True, default=True, max_length=50),
        ),
    ]