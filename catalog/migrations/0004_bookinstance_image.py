# Generated by Django 4.1.2 on 2022-11-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_bookinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
