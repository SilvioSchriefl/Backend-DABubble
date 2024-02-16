# Generated by Django 5.0.2 on 2024-02-16 16:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0004_alter_channel_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_channels', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='channel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
