# Generated by Django 4.0.2 on 2023-01-26 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0002_alter_todolist_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='todolist',
            name='time',
            field=models.TimeField(auto_now_add=True, default='12:12:12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
