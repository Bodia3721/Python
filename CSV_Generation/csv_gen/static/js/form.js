$(document).ready(() => {
        let name_sch = $('#name_sch').val();
        let rows_num = $('#rows').val();
        userId = $('#user_id').val();

        $('.table').delegate('#checkbox_1', 'change', function () {

            if (this.checked) {
                let ord1 = $(event.target).parent().prev().find('input').val();
                let name_c1 = $(event.target).parent().prev().prev().find('input').val();
                let type_c1 = $(event.target).parent().prev().prev().prev().find('option:selected').attr('value');
                console.log('ord1 = ' + ord1);
                console.log('name_c1 = ' + name_c1);
                console.log('type_c1 = ' + type_c1);
                $.ajax({
                    url: '/app/checkbox',
                    data: `ord1=${ord1}&name_c1=${name_c1}&type_c1=${type_c1}`,
                    success: (result) => {
                        console.log(result.ord1);
                    }
                });
            }
        });

        $('.table').delegate('#checkbox_2', 'change', function () {

            if (this.checked) {
                let ord2 = $(event.target).parent().prev().find('input').val();
                let name_c2 = $(event.target).parent().prev().prev().find('input').val();
                let type_c2 = $(event.target).parent().prev().prev().prev().find('option:selected').attr('value');
                console.log('ord2 = ' + ord2);
                console.log('name_c2 = ' + name_c2);
                console.log('type_c2 = ' + type_c2);
                $.ajax({
                    url: '/app/checkbox',
                    data: `ord2=${ord2}&name_c2=${name_c2}&type_c2=${type_c2}`,
                    success: (result) => {
                        console.log(result.ord1);
                    }
                });
            }

        });

});
