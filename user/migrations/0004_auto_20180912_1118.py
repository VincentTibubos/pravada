# Generated by Django 2.1 on 2018-09-12 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_auto_20180707_0334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='')),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('country', models.CharField(blank=True, default='', max_length=100)),
                ('organization', models.CharField(blank=True, default='', max_length=100)),
                ('reputation', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='role',
            name='org_id',
        ),
        migrations.RemoveField(
            model_name='role',
            name='staff_id',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
