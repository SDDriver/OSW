# Generated by Django 5.0.2 on 2024-03-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oswapp', '0018_remove_answers_right_check_question_right_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_count',
            field=models.IntegerField(default=0),
        ),
    ]
