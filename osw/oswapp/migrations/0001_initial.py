# Generated by Django 5.0.2 on 2024-02-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Введите номер вопроса', max_length=3, verbose_name='Номер вопроса')),
                ('text', models.CharField(help_text='Введите текст вопроса', max_length=100, verbose_name='Текст вопроса')),
                ('var1', models.CharField(help_text='Введите первый вариант ответа', max_length=100, verbose_name='Первый вариант ответа')),
                ('var2', models.CharField(help_text='Введите второй вариант ответа', max_length=100, verbose_name='Второй вариант ответа')),
                ('var3', models.CharField(help_text='Введите третий вариант ответа', max_length=100, verbose_name='Третий вариант ответа')),
                ('var4', models.CharField(help_text='Введите четвертый вариант ответа', max_length=100, verbose_name='Четвертый вариант ответа')),
                ('var5', models.CharField(help_text='Введите пятый вариант ответа', max_length=100, verbose_name='Пятый вариант ответа')),
                ('var6', models.CharField(help_text='Введите шестой вариант ответа', max_length=100, verbose_name='Шестой вариант ответа')),
                ('correct_var_number', models.CharField(help_text='Введите номер правильного ответа', max_length=3, verbose_name='Номер правильного ответа')),
                ('help_text', models.CharField(help_text='Введите текст помощи', max_length=100, verbose_name='Текст помощи')),
            ],
        ),
    ]