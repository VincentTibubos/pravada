# Generated by Django 2.1.1 on 2018-10-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20181007_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='cover',
            field=models.ImageField(blank=True, upload_to='uploads/publication/covers/%Y/%m/%d/'),
        ),
    ]
