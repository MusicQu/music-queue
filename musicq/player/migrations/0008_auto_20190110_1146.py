# Generated by Django 2.1.3 on 2019-01-10 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatrooms', '0010_remove_room_playlist'),
        ('player', '0007_auto_20190109_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='room',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chatrooms.Room'),
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='song',
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='player.Song'),
        ),
    ]
