# Generated by Django 5.0.2 on 2024-02-19 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0012_chat_channel_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='name',
        ),
    ]
