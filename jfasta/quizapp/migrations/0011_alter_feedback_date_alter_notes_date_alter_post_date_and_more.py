# Generated by Django 4.0.3 on 2022-04-19 05:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0010_alter_feedback_date_alter_notes_date_alter_post_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 8, 28, 13, 399831)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 8, 28, 13, 400750)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 8, 28, 13, 398756)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 8, 28, 13, 394764)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 8, 28, 13, 397755)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 8, 28, 13, 399831)),
        ),
    ]
