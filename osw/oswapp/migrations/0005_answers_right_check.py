# Generated by Django 5.0.2 on 2024-02-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oswapp', '0004_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='right_check',
            field=models.CharField(default=0, max_length=1),
        ),
    ]
