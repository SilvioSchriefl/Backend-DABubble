# Generated by Django 5.0.2 on 2024-02-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0017_remove_chat_channel_id_remove_message_chat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='messages',
            field=models.ManyToManyField(blank=True, null=True, related_name='chats', to='DABubble.message'),
        ),
    ]
