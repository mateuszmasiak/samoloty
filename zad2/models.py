# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
def clean1(t):
    for f in Flight.objects.all():
        if t > f.start_time and t< f.end_time:
            raise ValidationError(_('Two flights at the same time'))
        #if end_time >= f.start_time and end_time<= f.end_time:
        #    raise ValidationError(_('Two flights at the same time'))

class PlaneCrew(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)



class PlanesCrews(models.Model):
    rejestration_number = models.CharField(max_length=30)
    places = models.IntegerField()
    crew = models.ForeignKey(PlaneCrew, on_delete=models.CASCADE, default = 1)

class Plane(models.Model):
    rejestration_number = models.CharField(max_length=30)
    places = models.IntegerField()
    #crew = models.ForeignKey(PlaneCrew, on_delete=models.CASCADE, default = 1)

    def __str__(self):
        return self.rejestration_number
    def add(self):
        self.save()

class Flight(models.Model):
    crew_first_name = models.CharField(max_length=30, default = "Mateusz")
    crew_last_name = models.CharField(max_length=30, default = "Masiak")
    airport = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    #start_time = models.DateTimeField(validators=[clean1])
    #end_time = models.DateTimeField(validators=[clean1])
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE, default = 1)

    def clean(self):
        for f in Flight.objects.filter(plane = self.plane):
            if (self.start_time > f.start_time and self.start_time < f.end_time) or (self.end_time>f.start_time and self.end_time<f.end_time):
                raise ValidationError(_('Two flights at the same time of plane'))
            if  (self.start_time < f.start_time and self.end_time>f.start_time):
                raise ValidationError(_('Two flights at the same time of plane'))

        for f in Flight.objects.filter(crew_first_name = self.crew_first_name, crew_last_name = self.crew_last_name):
            if (self.start_time > f.start_time and self.start_time < f.end_time) or (self.end_time>f.start_time and self.end_time<f.end_time):
                raise ValidationError(_('Two flights at the same time of crew'))
            if  (self.start_time < f.start_time and self.end_time>f.start_time):
                raise ValidationError(_('Two flights at the same time of crew'))
        return super(Flight,self).clean()



    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Flight, self).save(*args, **kwargs)

    @classmethod
    def create(cls, airport, start_time,end_time, plane):
        flight = cls(airport = airport, start_time = start_time, end_time = end_time, plane = plane)
        flight.full_clean()
        return flight

class FlightPassenger(models.Model):
    places_purchased = models.IntegerField()
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
