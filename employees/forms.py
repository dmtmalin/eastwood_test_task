# -*- coding: utf-8 -*-
import django_filters
from employees.models import Employee


def is_worked_filter(queryset, value):
    return queryset.filter(
            end_work__isnull=value
    )


class EmployeeFilter(django_filters.FilterSet):
    is_worked = django_filters.BooleanFilter(action=is_worked_filter)

    class Meta:
        model = Employee
        fields = ['departament']







