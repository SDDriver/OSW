# Generated by Django 5.0.2 on 2024-03-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oswapp', '0015_alter_answers_user_answer_string'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='color_check',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='number',
        ),
        migrations.AddField(
            model_name='question',
            name='color_check',
            field=models.CharField(default=False, max_length=1),
        ),
    ]