const doCalculate = () => {
    let checkedCells = $('.check:checked');
    let totalPrice = 0;
    let sellItemsList = '';

    for (let cell of checkedCells){
        let parent =$(cell).parent().parent();
        totalPrice += parseFloat($(parent).find('td.price_cell').text());
        sellItemsList += $(parent).find('td.id_cell').text() + ',';
    }
    sellItemsList += totalPrice;

    console.log(`totalPrice = ${totalPrice}`);
    console.log(`sellItemsList = ${sellItemsList}`);
    $('#total').text(`${totalPrice.toFixed(2)} грн.`);
    $('#bill-btn').attr('href', `/orders/bill/${sellItemsList}`);
};


$(document).ready(() =>{

    console.log('CALC-items - start');
    doCalculate();

    $('.check').click((event) =>{
       console.log('INPUT_CHECK -> Click');
       doCalculate();
    });

});