# Generated by Django 3.2 on 2022-04-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
