# Generated by Django 4.0.4 on 2022-06-18 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0017_alter_feedback_date_alter_notes_date_alter_post_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='qtype',
            field=models.TextField(choices=[('h2h', 'H2H'), ('normal', 'Normal'), ('survival', 'Survival')], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 18, 51, 23, 557974)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 18, 51, 23, 559251)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 18, 51, 23, 552971)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 18, 51, 23, 552971)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 18, 51, 23, 552971)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 18, 51, 23, 557974)),
        ),
        migrations.AlterField(
            model_name='replyreplies',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 18, 51, 23, 559251)),
        ),
    ]
