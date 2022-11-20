# Generated by Django 3.2.13 on 2022-11-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_delete_notions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField(max_length=30)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]