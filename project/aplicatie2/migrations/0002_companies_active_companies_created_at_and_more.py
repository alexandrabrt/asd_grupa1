# Generated by Django 4.2.7 on 2023-11-21 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='companies',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companies',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]