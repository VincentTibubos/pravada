# Generated by Django 2.1.1 on 2018-10-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20181007_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='staff_id',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_followers',
            field=models.ManyToManyField(to='user.Profile'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('a', 'Administrator'), ('e', 'Editor'), ('m', 'Moderator'), ('s', 'Staff'), ('c', 'Contributor')], default='s', max_length=1),
        ),
    ]