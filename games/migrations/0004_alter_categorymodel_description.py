# Generated by Django 3.2.8 on 2022-01-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_categorymodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]