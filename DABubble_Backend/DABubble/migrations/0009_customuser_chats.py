# Generated by Django 5.0.2 on 2024-02-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0008_alter_channel_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='chats',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='DABubble.chat'),
        ),
    ]
