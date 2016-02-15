# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    index = models.CharField(max_length=1, db_index=True)
    surname = models.CharField(max_length=200, db_index=True)
    middle_name = models.CharField(max_length=200)
    birthday = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    begin_work = models.DateField()
    end_work = models.DateField(null=True, db_index=True)
    post = models.CharField(max_length=200)
    departament = models.ForeignKey(Departament)

    def save(self, *args, **kwargs):
        self.index = self.surname[0].upper()
        super(Employee, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s %s %s" % (self.surname, self.name, self.middle_name, )
