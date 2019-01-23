# Generated by Django 2.1.5 on 2019-01-23 00:41

from django.db import migrations, models
import teams.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to=teams.models.image_path)),
                ('city', models.CharField(max_length=20)),
                ('sport', models.CharField(max_length=20)),
            ],
        ),
    ]
