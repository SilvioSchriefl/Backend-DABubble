# Generated by Django 5.0.2 on 2024-02-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0020_alter_message_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
