from django.shortcuts import render
from items.models import Item
from django.core.mail import send_mail


def bill(request, sell_list: str):
    if request.method == 'GET':
        sell_list_str_array = sell_list.split(',')                        #['1','3','4','24500']
        sel_list_num_array = [int(x) for x in sell_list_str_array[:-1]]   #['1','3','4','24500'] => ['1','3','4']
        total_price = int(sell_list_str_array[-1])                        # 24500
        final_list = []

        for item_id in sel_list_num_array:
            item = Item.objects.get(id=item_id)
            final_list.append({
                'product_name': item.product.name,
                'category_name': item.product.category.name,
                'product_price': item.product.price,
                'product_photo': item.product.picture
            })

        return render(request, 'orders/bill.html', context={
            'title': 'Оформлення рахунку',
            'total_price': total_price,
            'final_list': final_list,
            'init_list': sell_list
        })


def confirm(request, init_list: str):
    if request.method == 'GET':
        return render(request, 'orders/confirm.html', context={
            'title': 'Підвтердження замовлення',
            'init_list': init_list
        })
    elif request.method == 'POST':
        email = request.POST['email']
        sell_list_str_array = init_list.split(',')
        sel_list_num_array = [int(x) for x in sell_list_str_array[:-1]]
        total_price = int(sell_list_str_array[-1])
        info_list = []

    for item_id in sel_list_num_array:
        item = Item.objects.get(id=item_id)
        info_list.append({
            'product_name': item.product.name,
            'category_name': item.product.category.name,
            'product_price': item.product.price
        })

    subject = 'Повідомлення про замовлення на сайті WebShop'
    body = """
        <h1>Повідомлення про замовлення на сайті WebShop</h1>
        <hr />
        <h2 style="color: black"> Ви підтвердили замовлення наступних товарів:</h2>
        <h3>
        <ol>
    """

    for info in info_list:
        body += f"""
            <li>{info.get('product_name')} / {info.get('category_name')} - {info.get('product_price')} грн.</li>
        """

    body += f"""
        </ol>
        </h3>
        <hr />
        <h2>Загальна сума до сплати: <span style="color: red">{total_price} грн.</span></h2>
    """

    success = send_mail(subject, '', 'WebShop', [email], fail_silently=False, html_message=body)
    if success:
        return render(request, 'orders/thanks.html', context={
            'title': 'Подяка за замовлення',
            'email': email
        })
    else:
        return render(request, 'orders/failed.html', context={
            'title': 'Помилка поштового відправлення'
        })
