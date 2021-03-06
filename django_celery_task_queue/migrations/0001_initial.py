# Generated by Django 3.0.2 on 2020-08-07 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_table', models.TextField()),
                ('task_id', models.IntegerField()),
                ('exc_type', models.TextField()),
                ('exc_value', models.TextField()),
                ('exc_traceback', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'task_queue_exc',
            },
        ),
    ]
