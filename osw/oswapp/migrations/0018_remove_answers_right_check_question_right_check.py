# Generated by Django 5.0.2 on 2024-03-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oswapp', '0017_alter_answers_right_check_alter_question_color_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='right_check',
        ),
        migrations.AddField(
            model_name='question',
            name='right_check',
            field=models.BooleanField(default=False),
        ),
    ]
