# Generated by Django 3.2.16 on 2023-04-02 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('components', '0004_delete_cartcomponentitemmodel'),
        ('games', '0011_delete_cartgameitemmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartGameItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BoughtModel_User', to=settings.AUTH_USER_MODEL)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BoughtModel_GamesModel', to='games.gamesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CartComponentItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CartComponentItemModel_User', to=settings.AUTH_USER_MODEL)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CartComponentItemModel_ComponentModel', to='components.componentsmodel')),
            ],
        ),
    ]
