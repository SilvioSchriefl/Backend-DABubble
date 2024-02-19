# Generated by Django 5.0.2 on 2024-02-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0016_remove_chat_messages_chat_channel_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='channel_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.AddField(
            model_name='chat',
            name='messages',
            field=models.ManyToManyField(related_name='chats', to='DABubble.message'),
        ),
    ]