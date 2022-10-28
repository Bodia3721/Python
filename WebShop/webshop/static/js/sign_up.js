function example() {
    // Вікно повідомлень:
    alert('Базове выкно повыдомлень');

    //консоль розробника:
    console.log('Повідомлення сценарію для JS-консолі')

    //Вікно введення даних:
    let client = prompt('Як вас звати?');
    console.log('Будемо знайомі, ' + client);

    //Підтвердження вибору
    let choice = confirm('Ви бажаєте перейти на сайт UKR.NET?');
    if (choice == true){
        window.location = 'https://www.ukr.net';
    }else{
        console.log('Ну і не треба!');
    }
}

$(document).ready(() =>{

    console.log('JQuery -> OK');

    let result1 = false;   //валідація логіну
    let result2 = false;   //валідація 1 пароля
    let result3 = false;   //валідація 2 пароля
    let result4 = false;   //валідація імейла

    //Валідація логіну
    $('#login').blur(() => {
        console.log('#login-blur -> OK');
        let loginX = $('#login').val();
        console.log('loginX -> ' + loginX);

        let loginRe = /^[a-zA-Z][a-zA-Z0-9_\-\.]{4,15}$/;
        if (loginRe.test(loginX)){
            //перевірка зайнятості логіну
            $.ajax({
                url: '/accounts/ajax_reg',
                data: 'login=' + loginX,
                success: (result)=>{
                    console.log('AJAX -> OK');
                    console.log(result.message);
                    if (result.message === 'зайнятий'){
                        $('#login_err').text('Логін зайнятий!');
                        result1 = false;
                    } else {
                        $('#login_err').text('');
                        result1 = true;
                    }
                }
            });
        }else{
            $('#login_err').text('Помилка формату логіна! Дозволений формат: a-z, A-Z, 0-9, _, -, .');
            result1 = false;
        }
    });

    // Валідація 1 пароля
    $('#pass1').blur(() => {
        console.log('#pass1-blur -> OK');
         let pass1X = $('#pass1').val();
        console.log('pass1X -> ' + pass1X);

        let passRe = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_\-\.])[a-zA-Z0-9_\-\.]{6,}$/;
        if (passRe.test(pass1X)) {
            $('#pass1_err').text('');
            result2 = true;
        }else{
            $('#pass1_err').text('Помилка формату пароля! Від 7 символів, хоча б одна: a-z, A-Z, 0-9, _, -, .');
            result2 = false;
        }
    });

     // Валідація 2 пароля
    $('#pass2').blur(() => {
        console.log('#pass2-blur -> OK');
        let pass1X = $('#pass1').val();
        let pass2X = $('#pass2').val();

        if (pass1X === pass2X) {
            $('#pass2_err').text('');
            result3 = true;
        }else{
            $('#pass2_err').text('Введені паролі не співпадають!');
            result3 = false;
        }
    });

    // Валідація e-mail
    $('#email').blur(() => {
        console.log('#email-blur -> OK');
        let emailX = $('#email').val();
        console.log('emailX -> ' +emailX);

        let emailRe = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        if (emailRe.test(emailX)){
            //перевірка зайнятості email
            $.ajax({
                url: '/accounts/ajax_reg_email',
                data: 'email=' + emailX,
                success: (result)=>{
                    console.log('AJAX -> OK');
                    console.log(result.message);
                    if (result.message === 'зайнятий'){
                        $('#email_err').text('E-mail зайнятий!');
                        result1 = false;
                    } else {
                        $('#email_err').text('');
                        result1 = true;
                    }
                }
            });
        }else{
            $('#email_err').text('Помилка формату e-mail!');
            result1 = false;
        }
    });


    $('#submit').click(() => {
        if (result1 && result2 && result3 && result4){
            $('#form1').attr('onsubmit', 'return true');
        } else {
            $('#form1').attr('onsubmit', 'return false');
            alert('Форма містить некоректні дані!\nВідправка даних заблокована!')
        }
    })

});
