# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


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

    def __unicode__(self):
        return "%s %s %s" % (self.surname, self.name, self.middle_name,)


@receiver(pre_save, sender=Employee)
def add_index(sender, instance, *args, **kwargs):
    instance.index = instance.surname[0].upper()
