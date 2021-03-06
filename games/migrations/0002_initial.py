# Generated by Django 3.2.8 on 2021-11-02 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisationmodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrganisationModel_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='GameModel_CategoryModel', to='games.categorymodel'),
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GameModel_OrganisationModel', to='games.organisationmodel'),
        ),
        migrations.AddField(
            model_name='boughtmodel',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BoughtModel_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='boughtmodel',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BoughtModel_GamesModel', to='games.gamesmodel'),
        ),
    ]
