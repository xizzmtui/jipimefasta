# Generated by Django 4.0.3 on 2022-04-14 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_feedback_img_alter_feedback_date_alter_post_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 14, 16, 54, 43, 727843)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 14, 16, 54, 43, 726845)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 14, 16, 54, 43, 724850)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 14, 16, 54, 43, 725849)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 14, 16, 54, 43, 727843)),
        ),
    ]
