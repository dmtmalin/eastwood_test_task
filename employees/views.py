# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from employees.models import Employee
from employees.components.group import get_groups
from employees.components.remember import get_minded_filter


# Предоставляет отфильтрованный список сотрудников в виде страниц
def employees_list(request):
    f = get_minded_filter(request)
    paginator = Paginator(f, 3)
    page = request.GET.get('page')
    try:
        e = paginator.page(page)
    except PageNotAnInteger:
        e = paginator.page(1)
    except EmptyPage:
        e = paginator.page(paginator.num_pages)
    return render(request, 'employees/employees.html', {'filter': f, 'employees': e})


# Предоставляет информацию о сотруднике по id
def employee(request, id):
    e = Employee.objects.get(id=id)
    return render(request, 'employees/employee.html', {'employee': e})


# Предоставляет сгруппированный список сотрудников по алфавиту
def index(request):
    employees = []
    number_groups = 7
    offset = request.GET.get('offset', 0)
    limit = request.GET.get('limit', 0)
    try:
        employees = Employee.objects.all().order_by('index')[offset:limit]
    except ValueError:
        pass
    alphabet_groups = get_groups(number_groups)
    context = {'employees': employees, 'alphabet_groups': alphabet_groups}
    return render(request, 'employees/index.html', context)
