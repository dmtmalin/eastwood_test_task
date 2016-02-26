from django.test import TestCase
from django.http import QueryDict
from employees.components.group import grouped, get_number_in_group, get_groups
from employees.forms import EmployeeFilter
from employees.models import Employee


class GroupedTestCase(TestCase):
    def setUp(self):
        self.group = [{'index': 'A', 'count': 4}, {'index': 'B', 'count': 4}]
        self.number_in_group = 2

    def test_grouped(self):
        groups = grouped(self.group, self.number_in_group)
        self.assertEquals(len(groups), 2)

    def test_employees_grouped(self):
        groups = get_groups(self.number_in_group)
        for g in groups:
            employees = Employee.objects.all()[g.offset:g.limit]
            if employees:
                index = g.name.split('-')
                self.assertEquals(index[0], employees[0].surname[0].upper())
                self.assertEquals(index[1], employees[::-1][0].surname[0].upper())

    def test_empty_grouped(self):
        empty_group = []
        groups = grouped(empty_group, self.number_in_group)
        self.assertEquals(len(groups), 0)


class NumberInGroupTestCase(TestCase):
    def setUp(self):
        self.group = [{'count': 4}, {'count': 4}]

    def test_number_in_group(self):
        number_groups = 2
        number = get_number_in_group(self.group, number_groups)
        self.assertEquals(number, 4)

    def test_error_number_in_group(self):
        error_number_in_group = 0
        self.assertRaises(ZeroDivisionError, get_number_in_group, self.group, error_number_in_group)


class EmployeeFilterTestCase(TestCase):
    def test_form(self):
        request_get = QueryDict('departament=1&is_worked=1')
        f = EmployeeFilter(request_get, queryset=Employee.objects.all().order_by('surname'))
        self.assertTrue(f.form.is_valid())
