# Generated by Django 5.0.2 on 2024-03-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oswapp', '0011_answers_color_remove_answers_color_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='help_text',
            field=models.CharField(help_text='Введите текст помощи', max_length=10000, verbose_name='Текст помощи'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(help_text='Введите текст вопроса', max_length=1000, verbose_name='Текст вопроса'),
        ),
        migrations.AlterField(
            model_name='question',
            name='var1',
            field=models.CharField(help_text='Введите первый вариант ответа', max_length=1000, verbose_name='Первый вариант ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='var2',
            field=models.CharField(help_text='Введите второй вариант ответа', max_length=1000, verbose_name='Второй вариант ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='var3',
            field=models.CharField(help_text='Введите третий вариант ответа', max_length=1000, verbose_name='Третий вариант ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='var4',
            field=models.CharField(blank=True, help_text='Введите четвертый вариант ответа', max_length=1000, null=True, verbose_name='Четвертый вариант ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='var5',
            field=models.CharField(blank=True, help_text='Введите пятый вариант ответа', max_length=1000, null=True, verbose_name='Пятый вариант ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='var6',
            field=models.CharField(blank=True, help_text='Введите шестой вариант ответа', max_length=1000, null=True, verbose_name='Шестой вариант ответа'),
        ),
    ]
