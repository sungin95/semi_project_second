# Generated by Django 3.2.13 on 2022-11-21 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='저장용량',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
