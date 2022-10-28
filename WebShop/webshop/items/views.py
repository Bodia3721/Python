from django.shortcuts import render
from django.http import JsonResponse
from .models import Item


def index(request):
    return render(request, 'items/index.html', context={
        'title': 'Перегляд кошика',
        'user_items': Item.objects.filter(user_id=request.user.id)
    })


def ajax_cart(request):
    response = dict()

    # Отримуємо значення get-параметрів із AJAX-запиту:
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')
    price = request.GET.get('price')

    # Зворотня перевірка
    response['uid'] = f'UID: {uid}'
    response['pid'] = f'PID: {pid}'
    response['price'] = f'price: {price}'

    # Зберігаємо товар доданий до кошика у БД
    Item.objects.create(
        user_id=uid,
        product_id=pid,
        status='Очікування замовлення'
    )
    response['create_mess'] = 'Товар збережений'

    # Зчитуємо з БД списку всіх товарів даного користувача

    user_items = Item.objects.filter(user_id=uid)

    # Обчислюємо вартість товарів даного користувача
    amount = 0
    for item in user_items:
        amount += item.product.price

    # Записуємо у відповідь сервера загальну кількість та вартість товарів користувача
    response['count'] = len(user_items)
    response['amount'] = amount

    # відправляємо відповідь клієнту:
    return JsonResponse(response)


def ajax_cart_display(request):
    uid = request.GET['uid']
    user_items = Item.objects.filter(user_id=uid)

    s = 0
    for item in user_items:
        s += item.product.price

    return JsonResponse({
        'uid_back': uid,
        'amount': s,
        'count': len(user_items)
    })


def ajax_del_item(request):
    item_id = request.GET['item_id']
    del_item = Item.objects.get(id=item_id)
    del_item.delete()
    return JsonResponse({
        'report': f'Товар із ID: {item_id} був видалений із кошика!'
    })

