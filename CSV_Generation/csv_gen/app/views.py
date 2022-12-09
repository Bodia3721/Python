import csv
from wsgiref import headers

import fake as fake
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from faker import Faker

from .models import Scheme


def index(request):
    if request.method == 'GET':
        return render(request, 'sign_in.html', context={
            'title': 'Authorization'
        })
    elif request.method == 'POST':

        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        remember = request.POST.get('remember')

        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            color = 'red'
            message = 'User not found!'
            return render(request, 'auth_report.html', context={
                'title': 'Authorization report',
                'color': color,
                'message': message
            })
        else:
            login(request, user)
            return redirect('/app/main')


def data_schemas(request):
    return render(request, 'data_schemas.html', context={

    })


def new_schemas(request):
    return render(request, 'new_schemas.html', context={

    })


def ajax_form(request):
    response = dict()

    name_sch = request.POST.get('name_sch')
    rows_num = request.POST.get('rows')

    # name_sch = request.GET.get('name_sch')
    # rows_num = request.GET.get('rows_num')

    ord1 = request.GET.get('ord1')
    name_c1 = request.GET.get('name_c1')
    type_c1 = request.GET.get('type_c1')
    ord2 = request.GET.get('ord2')
    name_c2 = request.GET.get('name_c2')
    type_c2 = request.GET.get('type_c2')

    Scheme.objects.create(
        col1=type_c1,
        name1=name_c1,
        ord1=ord1,
        name=name_sch,
        rows=rows_num,
        col2=type_c2,
        name2=name_c2,
        ord2=ord2,
    )
    # print({
    #     'name_sch': name_sch,
    #     'rows_num': rows_num,
    #     'ord1': ord1,
    #     'name_c1': name_c1,
    #     'type_c1': type_c1,
    #     'ord2': ord2,
    #     'name_c2': name_c2,
    #     'type_c2': type_c2,
    # })

    return JsonResponse(response)


def generate_csv(request):
    pass