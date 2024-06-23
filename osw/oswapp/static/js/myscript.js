// Проверка устройства юзера. Если устройство мобильное, то убираем стилевой класс, который
// жестко фиксирует высоту div с вопросом и вариантами ответов

function mobile_check() {

    const variants = document.getElementsByClassName('stab_container');
    var array_variants = Array.from(variants);

    const questions = document.getElementsByClassName('stab_container_2');
    var array_questions = Array.from(questions);

    const devices = new RegExp('Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini', "i");
    if (devices.test(navigator.userAgent)) {
      array_variants.forEach((elem) => {elem.classList.remove("stab_container")});
      array_questions.forEach((elem) => {elem.classList.remove("stab_container_2")});

    }
}

// Начальное модальное окно в билете

function question_window_ticket() {

   const myModalTicket = new bootstrap.Modal(document.getElementById('myModalTicket'), {backdrop: 'static', keyboard: false});
   myModalTicket.show();
}

// Начальное модальное окно в экзамене

function question_window_exam() {

   const myModalExam = new bootstrap.Modal(document.getElementById('myModalExam'), {backdrop: 'static', keyboard: false});
   myModalExam.show();
}

// Таймер экзамена

function timer() {

    var mins = document.getElementById("min");
    var secs = document.getElementById("sec");
    var s0 = secs.innerText;
    var m0 = mins.innerText;

    if (s0 == '' && m0 =='') {secs.innerText = '00'; mins.innerText = '20';}

    else
          {var s = parseInt(s0);
          var m = parseInt(m0);
          s -= 1;

          if (s == -1 && m >10 && m <= 20) {secs.innerText = '59';
                                            mins.innerText = m - 1}

          if (s == -1 && m > 0 && m <= 10) {secs.innerText = '59';
                                            mins.innerText = '0' + (m - 1)}

          if (s < 60 && s > 9) {secs.innerText = s}

          if (s < 10 && s >= 0) {secs.innerText = '0' + s}

          if (m == 0 && s == -1) {

                  const myModalTimeOver = new bootstrap.Modal(document.getElementById('myModalTimeOver'), {backdrop: 'static', keyboard: false});
                  return myModalTimeOver.show();}
            }

    setTimeout(timer, 1000);
}

//Функция выхода из модального окна после окончания времени экзамена

function timeIsOver() {
    var my_form = document.getElementById("my_form_exam");
    return (my_form.submit())
}

// Функция для смены div с вопросами при помощи кнопки "Следующий вопрос"

function questionSwitch(n) {
	
	var count = n;
	count += 1;

	var div_prev = document.getElementById(n);
	div_prev.setAttribute("hidden", "");

	var div_nxt = document.getElementById(count);
	div_nxt.removeAttribute("hidden", "")
	}

// Функция для смены div с вопросами при помощи нумерованных кнопок под вопросами

function questionSwitch2(k) {

	var y = 1;
	let array = [];

    try {
        for(x = 0; x < 22; x++) {array[x] = y.toString();
                                 y += 1;}
        } catch (e) {} // Здесь и далее перехват исключения для пропуска ошибки наличия 21 и 22 вопросов в билетах 1-8

	var div_to_open = document.getElementById(k);
	div_to_open.removeAttribute("hidden", "");
	
	array.splice(k-1, 1);

	try {
        for (i = 0; i < 21; i++) { var div_to_hide = document.getElementById(array[i]);
                                   div_to_hide.setAttribute("hidden", "");}
        } catch (e) {}
}

// Массив с id всех чекбоксов для использования в функциях

let checkboxes_array = []

for (i = 0; i < 22; i++) {
    let question_array = [];
    checkboxes_array[i] = question_array;
    for (x = 0; x < 6; x++) {
        checkboxes_array[i][x] = `answer${x + 1}` + `_${i + 1}`
    }
}

// Функция для закрашивания нумерованных кнопок под вопросами вследствие выбора чекбокса соответствующего вопроса
// Вызывается при нажатии на кнопку "Следующий вопрос" и любой нумерованной кнопки

function btnPaint() {

	var check;
	var btn_to_paint;

    try {
        for (i = 0; i < 22; i++) {

            var amount_checks = 0;
            var unpainted_checks = 0;

            for (x = 0; x < 6; x++) {

                check = document.getElementById(checkboxes_array[i][x]);

                if (check != null) {
                    amount_checks += 1;

                    if (check.checked) {

                        btn_to_paint = document.getElementById(`btn${i + 1}`);
                        btn_to_paint.classList.remove('btn_paint');
                        btn_to_paint.classList.add('btn_paint_secondary');
                        }
                    else {	unpainted_checks += 1;}
                    }

            if (unpainted_checks == amount_checks) {
                btn_to_paint = document.getElementById(`btn${i + 1}`);
                btn_to_paint.classList.remove('btn_paint_secondary');
                btn_to_paint.classList.add('btn_paint');
                }

                }
            }
        } catch (e) {}
	}

// Функция для проверки факта ответа на все вопросы билета

function full_pass_checking_ticket() {

        // Проверяем на все ли вопросы был дан ответ

	    var check;
		var checked_flag;
		var full_check;
		var questions_quantity;
		var is_ninth_ticket = document.getElementById('21');

		if (is_ninth_ticket == true) {questions_quantity = 22}
		else {questions_quantity = 20}

		try {

            for (i = 0; i < questions_quantity; i++) {

                checked_flag = 0;

                for (x = 0; x < 6; x++) {

                    check = document.getElementById(checkboxes_array[i][x]);

                    if (check != null) {
                        if (check.checked) {checked_flag += 1;}
                        }
                    }

                // Если есть хотя бы один вопрос без выбранного чекбокса, отменяем submit и выводим модальное окно №1

                if (checked_flag == 0) {
                    full_check = false;
                    event.preventDefault();
                    const myModalTicketExit = new bootstrap.Modal(document.getElementById('myModalTicketExit'), {backdrop: 'static', keyboard: false});
                    return myModalTicketExit.show();
                    }
                }
            } catch (e) {}

        // Если на всех вопросах выбран хотя бы один чексбокс, отменяем submit и выводим модальное окно №2

        event.preventDefault();
        const myModalTicketExit2 = new bootstrap.Modal(document.getElementById('myModalTicketExit2'), {backdrop: 'static', keyboard: false});
        return myModalTicketExit2.show();

	}

// Функция для проверки факта ответа на все вопросы экзамена

function full_pass_checking_exam() {

        // Проверяем на все ли вопросы был дан ответ

	    var check;
		var checked_flag;
		var full_check;


        try {
            for (i = 0; i < 20; i++) {

                checked_flag = 0;

                for (x = 0; x < 6; x++) {

                    check = document.getElementById(checkboxes_array[i][x]);

                    if (check != null) {
                        if (check.checked) {checked_flag += 1}
                        }
                    }

                // Если есть хотя бы один вопрос без выбранного чекбокса, отменяем submit и выводим модальное окно №1

                if (checked_flag == 0) {
                    full_check = false;
                    event.preventDefault();
                    const myModalExamExit = new bootstrap.Modal(document.getElementById('myModalExamExit'), {backdrop: 'static', keyboard: false});
                    return myModalExamExit.show();
                    }
                }
            } catch (e) {}

        // Если на всех вопросах выбран хотя бы один чексбокс, отменяем submit и выводим модальное окно №2

        event.preventDefault();
        const myModalExamExit2 = new bootstrap.Modal(document.getElementById('myModalExamExit2'), {backdrop: 'static', keyboard: false});
        return myModalExamExit2.show();
}

// Завершение билета и экзамена из модального окна

function exit(form_id) {
    var my_form = document.getElementById(form_id);
    return (my_form.submit());
}

// Завершение просмотра окна с результатами

function exit_from_result(to_page) {

    if (to_page == 'to_main_page') {
         var button = document.getElementById("button_res_exit");
         button.setAttribute("onclick", "location.href = '/'");
    }

    else {var button = document.getElementById("button_res_exit");
         button.setAttribute("onclick", "location.href = '/test/'");}

    const myModalResultExit = new bootstrap.Modal(document.getElementById('myModalResultExit'), {backdrop: 'static', keyboard: false});
    return myModalResultExit.show();
}

// Функция для закрашивания нумерованных кнопок в красный и зеленый цвет на странице результата

function btnPaintResult() {

	var check;
	var btn_to_paint;

    try {
        for (i = 0; i < 22; i++) {

            var red_count = 0; // Переменная для кол-ва выбранных юзером неправильных вариантов
            var checked_flag = 0; // Переменная для кол-ва выбранных юзером вариантов
            var green_label = 0; // Переменная для кол-ва правильных вариантов

            for (x = 0; x < 6; x++) {

                check = document.getElementById(checkboxes_array[i][x]);

                if (check != null) {
                    if (check.children[0] != null) {
                        if (check.children[0].getAttribute("checked") == '') {

                        checked_flag += 1;}
                        };

                    if (check.children[2] != null) {

                        // Если хотя бы один из вариантов имеет стилевой класс неправильно выбранного варианта,
                        // то закрашиваем кнопку вопроса в красный  и добавляем +1 в счетчик неправильных вариантов юзера

                        if (check.children[2].getAttribute("class") == "bg_label_false") {
                            btn_to_paint = document.getElementById(`btn${i + 1}`);
                            btn_to_paint.classList.add('btn_paint_lightcoral');
                            red_count += 1;
                            }

                        // Через стилевой класс получаем правильных вариантов для сопоставления далее с кол-вом ответов, выбранных юзером

                        if (check.children[2].getAttribute("class") == "bg_label_true") {
                                green_label += 1;
                                }
                        }
                    }

            }

            // Если неправильно выбранных вариантов в воросе нет, то закрашиваем кнопку вопроса в зеленый

            if (red_count == 0) {btn_to_paint = document.getElementById(`btn${i + 1}`);
                                 btn_to_paint.classList.add('btn_paint_neongreen');}

            // Если юзер выбрал меньше вариантов, чем правильных или вообще ни одного, то кнопка вопроса закрашивается в красный

            if (checked_flag < green_label || checked_flag == 0) {btn_to_paint = document.getElementById(`btn${i + 1}`);
                                    btn_to_paint.classList.add('btn_paint_lightcoral');}
            }

    } catch (e) {}
}

// Функция перехвата перемещения назад пользователем со страницы билета и экзамена

function back_intercept(modal_id, result_or_not = null) {

    history.pushState(null, null, null); // Добавляем новую запись в историю текущего окна с нулевыми изменениями

    window.addEventListener("popstate", function(event) { //Перехватываем popstate (также происходит переход на 1 позицию истории назад)

        history.pushState(null, null, null); // Снова добавляем запись в историю на случай, если юзер снова пойдет назад

        if (result_or_not == 'result_window') { // Отдельно определяем модальное окно для страницы результата

            var elt;
            if (elt = document.getElementById("to_main_page"))
                {to_page = 'to_main_page';}
            if (elt = document.getElementById("to_ticket_page"))
                {to_page = 'to_ticket_page';}
            exit_from_result(to_page);
        }

        else {
            const myModalExit = new bootstrap.Modal(document.getElementById(modal_id), {backdrop: 'static', keyboard: false});
            return myModalExit.show(); // Вызываем модальное окно
        }

    });
}

