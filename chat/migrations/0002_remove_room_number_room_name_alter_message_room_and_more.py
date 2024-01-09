# Generated by Django 4.2.5 on 2024-01-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='number',
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
