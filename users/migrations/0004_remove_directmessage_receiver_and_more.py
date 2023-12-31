# Generated by Django 4.2.7 on 2023-12-07 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_directmessage_receiver_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directmessage',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='directmessage',
            name='sender',
        ),
        migrations.CreateModel(
            name='ChatList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1_chats', to='users.profile')),
                ('user_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2_chats', to='users.profile')),
            ],
            options={
                'verbose_name_plural': 'چت ها',
            },
        ),
        migrations.AddField(
            model_name='directmessage',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='users.chatlist'),
        ),
    ]
