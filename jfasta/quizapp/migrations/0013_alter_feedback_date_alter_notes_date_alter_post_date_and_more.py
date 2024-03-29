# Generated by Django 4.0.3 on 2022-04-21 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0012_alter_feedback_date_alter_notes_date_alter_post_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 15, 8, 58, 733115)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 15, 8, 58, 734112)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 15, 8, 58, 732118)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 15, 8, 58, 730124)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 15, 8, 58, 731121)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 15, 8, 58, 733115)),
        ),
    ]
