# Generated by Django 4.0.3 on 2022-04-21 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0014_post_reply_count_reply_content_alter_feedback_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reply_count',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 16, 15, 56, 178931)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 16, 15, 56, 178931)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 16, 15, 56, 178931)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 16, 15, 56, 178931)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 16, 15, 56, 178931)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 16, 15, 56, 178931)),
        ),
    ]