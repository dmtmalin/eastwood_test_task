# -*- coding: utf-8 -*-
from django.db.models import Count
from employees.models import Employee


class AlphabetGroups(object):
    class Group(object):
        def __init__(self, offset, limit, name):
            self.offset = offset
            self.limit = limit
            self.name = name

    def __init__(self, number_groups):
        self.number_groups = number_groups
        self.groups = []
        self.number_in_group = 0
        self.group_count = Employee.objects.all().values('index').annotate(count=Count('id')).order_by('index')
        self.set_number_in_group()
        self.offset = 0
        self.offset_name = self.group_count[0]['index'] if len(self.group_count) > 0 else ''
        self.limit = 0
        self.limit_name = ''
        self.grouped()

    def grouped(self):
        sum_count = 0
        for i in range(len(self.group_count)):
            item = self.group_count[i]
            if sum_count <= self.number_in_group:
                self.limit += item['count']
                self.limit_name = item['index']
                sum_count += item['count']
                if self.is_last_item(i):
                    self.append_group()
            else:
                self.append_group()
                self.offset = self.limit
                self.offset_name = item['index']
                self.limit += item['count']
                self.limit_name = self.offset_name
                sum_count = item['count']

    def set_number_in_group(self):
        count = 0
        for item in self.group_count:
            count += item['count']
        self.number_in_group = int(count / self.number_groups)
        if self.number_in_group == 0:
            self.number_in_group = 1

    def append_group(self):
        name = '%s-%s' % (self.offset_name, self.limit_name, )
        group = AlphabetGroups.Group(self.offset, self.limit, name)
        self.groups.append(group)

    def is_last_item(self, i):
        return i + 1 >= len(self.group_count)

