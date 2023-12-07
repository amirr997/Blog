# Generated by Django 4.2.7 on 2023-12-07 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_directmessage_sender'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='users.chatlist')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='users.profile')),
            ],
            options={
                'verbose_name_plural': 'پیام ها',
            },
        ),
        migrations.DeleteModel(
            name='DirectMessage',
        ),
    ]
