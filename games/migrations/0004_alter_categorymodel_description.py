# Generated by Django 3.2.8 on 2021-11-17 10:07

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
