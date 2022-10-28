$(document).ready(() =>{

    console.log('jQuery/display - OK');

    const userID = $('#user_id').val();
    console.log('AllUserID- ' + userID);

    $.ajax({
        url: '/items/ajax_cart_display',
        data: `uid=${userID}`,
        success: (result) => {
            console.log('AJAX-ALL - OK');
            console.log('UID_BACK: ' + result.uid_back);
            console.log('count: ' + result.count);
            console.log('amount: ' + result.amount)

            $('#cart-count').text(result.count);
            $('.cart-summary').find('h5').text(result.count  + ' товарів обрано');
            $('.cart-summary').find('h4').text('ВАРТІСТЬ: ' + result.amount + ' грн.');
        }
    });

});