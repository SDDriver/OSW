from django.shortcuts import render
from .models import Question
import random

# Главная страница

def index(request):
    return render(request, template_name='index.html')

# Страница теории (тема)

def theme(request, themeid):
    return render(request, template_name=f'themes/theme{themeid}.html')

# Страница выбора билета

def testmain(request):

   return render(request,
                 template_name='test_main.html')

# Функция подготовки вопроса для билета и для экзамена (принимает список с номерами вопросов, возвращает заготовку контекста)

def making_of_questions(questions_num_list):

    context = {}
    i = 1

    for questionid in questions_num_list:

        info = Question.objects.get(number=questionid)

        q = info.text
        v1 = info.var1
        v2 = info.var2
        v3 = info.var3
        v4 = info.var4
        if v4 == None:
            v4 = ''
            context[f'hidden_4_{i}'] = True
        v5 = info.var5
        if v5 == None:
            v5 = ''
            context[f'hidden_5_{i}'] = True
        v6 = info.var6
        if v6 == None:
            v6 = ''
            context[f'hidden_6_{i}'] = True

        help_text = info.help_text

        context[f'q_{i}'] = q
        context[f'v1_{i}'] = v1
        context[f'v2_{i}'] = v2
        context[f'v3_{i}'] = v3
        context[f'v4_{i}'] = v4
        context[f'v5_{i}'] = v5
        context[f'v6_{i}'] = v6
        context[f'help_text_{i}'] = help_text

        i += 1

    return context

# Функция тестирования (билет)

def test_new(request, ticketid):

    # Определяем переменную для кол-ва вопросов в билете (в 9-м 22 вопроса)

    if ticketid == '9':
        q_quantity = 22
    else:
        q_quantity = 20  # Количество вопросов в стандартном билете (1-8)

    # Если POST запрос, то готовим шаблон с результатами тестирования

    if request.method == "POST":

        # Используя переменную ticketid создаем список с номерами вопросов билета

        first_question_id = 20 * int(ticketid) - 19
        questions_num_list = []
        for i in range(q_quantity):
            questions_num_list.append(first_question_id)
            first_question_id += 1

        # Используя номера вопросов подготавливаем заготовку контекста, а также отправляем на шаблон результата заголовок "Билет №"

        context = making_of_questions(questions_num_list)
        context['ticket_or_exam'] = f'Билет № {ticketid}'

        # Извлекаем из формы все значения выбранных чекбоксов в строку (для одного вопроса),
        # а затем строки в список (для всего билета)

        tickets_list = []
        for question_num in range(1, q_quantity + 1):
            answers_string = ''

            for var in range(1, 7):
                data = request.POST.get(f'field{var}_{question_num}')

                if data != None:
                    answers_string += data

            tickets_list.append(answers_string)

        # Извлекаем из БД строки с правильными ответами и также добавляем их в список

        tickets_list_correct = []
        questionid = 20 * int(ticketid) - 19
        for z in range(q_quantity):
            info = Question.objects.get(number=questionid)
            corvar = info.correct_var_number
            tickets_list_correct.append(corvar.replace('0', '').replace(' ', ''))
            questionid += 1

        # Подсчитываем общее кол-во правильных ответов для отображения на странице результата

        correct_amount = 0

        for i in range(len(tickets_list)):
            if tickets_list[i] == tickets_list_correct[i]:
                correct_amount += 1
        context['correct_amount'] = correct_amount
        if ticketid == '9':
            context['questions_in_ticket'] = 22
            ninth_ticket = 1
            context['ninth_ticket'] = ninth_ticket
        else:
            context['questions_in_ticket'] = 20

        # Создаем список ответов юзера из строки

        for question_num in range(1, q_quantity + 1):
            user_answer_list = ['0', '0', '0', '0', '0', '0']
            user_answer = tickets_list[question_num-1]

            n = 0
            for x in range(6):
                for z in user_answer:
                    if z == str(n + 1):
                        user_answer_list[n] = z
                n += 1

            # Создаем список из правильных ответов аналогично

            corvar_list = ['0', '0', '0', '0', '0', '0']
            corvar = tickets_list_correct[question_num-1]

            n = 0
            for x in range(6):
                for z in corvar:
                    if z == str(n + 1):
                        corvar_list[n] = z
                n += 1

            # Сравниваем списки справильными и неправильными ответами и готовим данные для отправки на шаблон

            bool_true = 1  # Переменная для логического выбора на шаблоне html

            for var in range(1, 7):
                if corvar_list[var-1] != '0' and user_answer_list[var-1] == '0':  # Вариант правильный, но пользователь не угадал
                    context[f'v{var}_{question_num}_true_failed'] = bool_true
                if corvar_list[var-1] != '0' and user_answer_list[var-1] != '0':  # Вариант правильный и пользователь угадал
                    context[f'v{var}_{question_num}_true'] = bool_true
                if corvar_list[var-1] == '0' and user_answer_list[var-1] != '0':  # Вариант неправильный, выбран пользователем
                    context[f'v{var}_{question_num}_false'] = bool_true

        return render(request,
                      'result_new.html',
                      context=context)

    # Если GET запрос, то формируем шаблон с вопросами билета

    else:

        # Используя переменную ticketid создаем список с номерами вопросов билета

        first_question_id = 20 * int(ticketid) - 19
        questions_num_list = []
        for i in range(q_quantity):
            questions_num_list.append(first_question_id)
            first_question_id += 1

        # Используя номера вопросов подготавливаем заготовку контекста

        context = making_of_questions(questions_num_list)
        context['ticketid'] = ticketid
        if ticketid == '9':
            context['num_of_questions'] = 22
            ninth_ticket = 1
            context['ninth_ticket'] = ninth_ticket
        else:
            context['num_of_questions'] = 20

        return render(request,
                      'test_new.html',
                      context=context)

# Экзамен

def exam(request):

    # Если POST запрос, то готовим шаблон с результатами экзамена

    if request.method == "POST":

        # Извлекаем строку с номерами вопросов, из которых был сформирован экзаменационный билет

        questions_num_string = request.POST.get('questions_num_string')
        questions_num_list = questions_num_string.rstrip(',').split(',')

        # Используя номера вопросов подготавливаем заготовку контекста, а также отправляем на шаблон результата заголовок "Экзамен"

        context = making_of_questions(questions_num_list)
        context['ticket_or_exam'] = 'Экзамен'

        # Извлекаем из формы все значения выбранных чекбоксов в строку (для одного вопроса),
        # а затем строки в список (для всего билета)

        tickets_list = []
        for question_num in range(1, 21):
            answers_string = ''

            for var in range(1, 7):
                data = request.POST.get(f'field{var}_{question_num}')

                if data != None:
                    answers_string += data

            tickets_list.append(answers_string)

        # Извлекаем из БД строки с правильными ответами и также добавляем их в список

        tickets_list_correct = []
        for z in range(20):
            info = Question.objects.get(number=int(questions_num_list[z]))
            corvar = info.correct_var_number
            tickets_list_correct.append(corvar.replace('0', '').replace(' ', ''))

        # Подсчитываем общее кол-во правильных ответов для отображения на странице результата

        correct_amount = 0
        for i in range(len(tickets_list)):
            if tickets_list[i] == tickets_list_correct[i]:
                correct_amount += 1
        context['correct_amount'] = correct_amount
        context['questions_in_ticket'] = 20

        # В зависимости от кол-ва правильных ответов готовим сообщение о сдаче/несдаче экзамена

        if correct_amount >= 18:
            exam_passed = True
            context['exam_passed'] = exam_passed
        else:
            exam_failed = True
            context['exam_failed'] = exam_failed

        # Создаем вписок ответов юзера из строки

        for question_num in range(1, 21):
            user_answer_list = ['0', '0', '0', '0', '0', '0']
            user_answer = tickets_list[question_num-1]

            n = 0
            for x in range(6):
                for z in user_answer:
                    if z == str(n + 1):
                        user_answer_list[n] = z
                n += 1

            # Создаем список из правильных ответов аналогично

            corvar_list = ['0', '0', '0', '0', '0', '0']
            corvar = tickets_list_correct[question_num-1]

            n = 0
            for x in range(6):
                for z in corvar:
                    if z == str(n + 1):
                        corvar_list[n] = z
                n += 1

            # Сравниваем списки с правильными и неправильными ответами и готовим данные для отправки на шаблон

            bool_true = 1  # Переменная для логического выбора на шаблоне html

            for var in range(1, 7):
                if corvar_list[var-1] != '0' and user_answer_list[var-1] == '0':  # Вариант правильный, но пользователь не угадал
                    context[f'v{var}_{question_num}_true_failed'] = bool_true
                if corvar_list[var-1] != '0' and user_answer_list[var-1] != '0':  # Вариант правильный и пользователь угадал
                    context[f'v{var}_{question_num}_true'] = bool_true
                if corvar_list[var-1] == '0' and user_answer_list[var-1] != '0':  # Вариант неправильный, выбран пользователем
                    context[f'v{var}_{question_num}_false'] = bool_true

            # Переменная для отображения на шаблоне результата div блока, который при нажатии кнопки "Завершить"
            # направит пользователя на главную страницу, а не на список билетов

            to_main_page = 1
            context['to_main_page'] = to_main_page

        return render(request,
                      'result_new.html',
                      context=context)

    # Если GET запрос, то формируем шаблон с вопросами экзамена

    else:

        # Используя random готовим список из 20 номеров вопросов

        questions_num_list = []
        while len(questions_num_list) < 20:
            question_number = random.randint(1, 182)
            if question_number in questions_num_list:
                continue
            else:
                questions_num_list.append(question_number)

        # Используя номера вопросов подготавливаем заготовку контекста

        context = making_of_questions(questions_num_list)

        # Отправляем на шаблон строку с номерами вопросов для последующего ее использвания
        # при подготовке результата после получения POST запроса

        questions_num_string = ''
        for i in range(20):
            questions_num_string += f'{str(questions_num_list[i])},'
        context['questions_num_string'] = questions_num_string

        return render(request,
                      'exam.html',
                      context=context)








