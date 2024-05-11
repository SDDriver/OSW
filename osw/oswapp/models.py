from django.db import models

class Question(models.Model):

    number = models.IntegerField(
                              help_text='Введите номер вопроса',
                              verbose_name='Номер вопроса')
    text = models.CharField(max_length=1000,
                            help_text='Введите текст вопроса',
                            verbose_name='Текст вопроса')
    var1 = models.CharField(max_length=1000,
                            help_text='Введите первый вариант ответа',
                            verbose_name='Первый вариант ответа')
    var2 = models.CharField(max_length=1000,
                            help_text='Введите второй вариант ответа',
                            verbose_name='Второй вариант ответа')
    var3 = models.CharField(max_length=1000,
                            help_text='Введите третий вариант ответа',
                            verbose_name='Третий вариант ответа')
    var4 = models.CharField(max_length=1000,
                            help_text='Введите четвертый вариант ответа',
                            verbose_name='Четвертый вариант ответа',
                            null=True,
                            blank=True)
    var5 = models.CharField(max_length=1000,
                            help_text='Введите пятый вариант ответа',
                            verbose_name='Пятый вариант ответа',
                            null=True,
                            blank=True)
    var6 = models.CharField(max_length=1000,
                            help_text='Введите шестой вариант ответа',
                            verbose_name='Шестой вариант ответа',
                            null=True,
                            blank=True)
    correct_var_number = models.CharField(max_length=6,
                             help_text='Введите номер правильного ответа',
                             verbose_name='Номер правильного ответа')
    help_text = models.CharField(max_length=10000,
                                 help_text='Введите текст помощи',
                                 verbose_name='Текст помощи')

    def __str__(self):
        return self.text


