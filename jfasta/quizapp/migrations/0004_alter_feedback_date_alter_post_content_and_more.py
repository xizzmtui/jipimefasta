# Generated by Django 4.0.3 on 2022-04-13 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_alter_feedback_date_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 14, 25, 17, 672748)),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 14, 25, 17, 670749)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='New Post', max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 14, 25, 17, 668751)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 14, 25, 17, 669750)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 14, 25, 17, 671749)),
        ),
    ]
