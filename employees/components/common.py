# -*- coding: utf-8 -*-
from django.db.models import Count
from employees.models import Employee


class AlphabetGroups(object):
    class Group(object):
        def __init__(self, offset, limit, name):
            self.offset = offset
            self.limit = limit
            self.name = name

    @staticmethod
    def get_groups(number_groups):
        group_employees = Employee.objects.all().values('index').annotate(count=Count('id')).order_by('index')
        number_in_group = AlphabetGroups.get_number_in_group(group_employees, number_groups)
        groups = AlphabetGroups.grouped(group_employees, number_in_group)
        return groups

    @staticmethod
    def grouped(group_employees, number_in_group):
        groups = []
        offset = 0
        offset_name = group_employees[0]['index'] if len(group_employees) > 0 else ''
        limit = 0
        limit_name = ''
        sum_count = 0
        for i in range(len(group_employees)):
            item = group_employees[i]
            if sum_count <= number_in_group:
                limit += item['count']
                limit_name = item['index']
                sum_count += item['count']
                if is_last_item(i, group_employees):
                    group = AlphabetGroups.new_group(offset, offset_name,
                                                     limit, limit_name)
                    groups.append(group)

            else:
                group = AlphabetGroups.new_group(offset, offset_name,
                                                 limit, limit_name)
                groups.append(group)
                offset = limit
                offset_name = item['index']
                limit += item['count']
                limit_name = offset_name
                sum_count = item['count']
        return groups

    @staticmethod
    def get_number_in_group(group_employees, number_groups):
        count = 0
        for item in group_employees:
            count += item['count']
        number_in_group = round(count / number_groups)
        return number_in_group if number_in_group > 0 else 1

    @staticmethod
    def new_group(offset, offset_name, limit, limit_name):
        name = '%s-%s' % (offset_name, limit_name, )
        group = AlphabetGroups.Group(offset, limit, name)
        return group


def is_last_item(i, arr):
    return i + 1 >= len(arr)

