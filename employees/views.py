# -*- coding: utf-8 -*-
from employees.forms import EmployeeFilter
from django_filters.views import FilterView
from django.views.generic import ListView
from employees.models import Employee
from employees.components.group import get_groups
from employees.components.minded import get_minded_request


# Предоставляет отфильтрованный список сотрудников в виде страниц
class EmployeeList(FilterView):
    filterset_class = EmployeeFilter
    context_object_name = 'employees'
    template_name = 'employees/employee_list.html'
    paginate_by = 3

    def get_filterset(self, filterset_class):
        r = get_minded_request(self.request)
        return filterset_class(r, queryset=Employee.objects.all().order_by('surname'))


# Предоставляет сгруппированный список сотрудников по алфавиту
class IndexList(ListView):
    template_name = 'employees/index.html'
    context_object_name = 'employees'
    number_groups = 7

    def get_context_data(self, **kwargs):
        context = super(IndexList, self).get_context_data(**kwargs)
        context['alphabet_groups'] = get_groups(self.number_groups)
        return context

    def get_queryset(self):
        offset, limit = self.request.GET.get('offset', 0), self.request.GET.get('limit', 0)
        employees = []
        try:
            employees = Employee.objects.all().order_by('index')[offset:limit]
        except ValueError:
            pass
        return employees
