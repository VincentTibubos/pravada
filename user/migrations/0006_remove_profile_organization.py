# Generated by Django 2.1 on 2018-09-12 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_organization_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='organization',
        ),
    ]
