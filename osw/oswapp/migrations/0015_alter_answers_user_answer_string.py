# Generated by Django 5.0.2 on 2024-03-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oswapp', '0014_delete_answers_color_answers_color_check_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='user_answer_string',
            field=models.CharField(default='', max_length=6),
        ),
    ]
