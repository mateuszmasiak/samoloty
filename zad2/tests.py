from datetime import datetime
from django.test import TestCase
from .models import *
import unittest

class TestValidationMethods(unittest.TestCase):
    def test_mytest(self):
        try:
            pl = Plane.objects.create(rejestration_number='123456', places = 23)
            lotnisko = 'l'
            start = datetime(2009,1,1,1,1,3)
            koniec = datetime(2011,1,1,1,1,3)
            imie='imie'
            nazwisko='nazwisko'
            Flight.objects.create(airport = lotnisko, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)

            lotnisko = 'l'
            start = datetime(2010,1,1,1,1,3)
            koniec = datetime(2010,1,2,1,1,3)
            imie='imie'
            nazwisko='nazwisko1'
            Flight.objects.create(airport = lotnisko, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)
            self.fail("powinien zostac zwrocony blad a nie zostal")
        except ValidationError:
        	pass


    def test_mytest1(self):
        try:
            pl = Plane.objects.create(rejestration_number='123456', places = 23)
            lotnisko = 'l'
            start = datetime(2006,1,1,1,1,3)
            koniec = datetime(2016,1,2,1,1,3)
            imie='testoweImie'
            nazwisko='testoweNazwisko'
            Flight.objects.create(airport = lotnisko, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)
            pl = Plane.objects.create(rejestration_number='123456', places = 23)
            lotnisko = 'l'
            start = datetime(2010,1,1,1,1,3)
            koniec = datetime(2010,1,2,1,1,3)
            imie='testoweImie'
            nazwisko='testoweNazwisko'
            Flight.objects.create(airport = lotnisko, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)
            self.fail("powinien zostac zwrocony blad a nie zostal")
        except ValidationError:
            pass

    def test_mytest2(self):
        try:
            pl = Plane.objects.create(rejestration_number='123456', places = 23)
            lotnisko = 'l'
            start = datetime(2009,1,1,1,1,3)
            koniec = datetime(2010,1,1,1,1,3)
            imie='imie2'
            nazwisko='nazwisko'
            Flight.objects.create(airport = lotnisko, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)
            start = datetime(2011,1,1,1,1,3)
            koniec = datetime(2011,1,2,1,1,3)
            imie='imie'
            nazwisko='nazwisko2'
            Flight.objects.create(airport = lotnisko, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)
            pass
        except ValidationError:
            self.fail(" nie powinien zostac zwrocony blad a zostal")


    def test_mytest3(self):
        try:
            pl = Plane.objects.create(rejestration_number='123456', places = 23)
            lotnisko = 'l'
            start = datetime(2009,1,1,1,1,3)
            koniec = datetime(2010,1,1,1,1,3)
            imie='imie2'
            nazwisko='nazwisko2'
            Flight.objects.create(airport = lotnisko, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)
            start = datetime(2011,1,1,1,1,3)
            koniec = datetime(2011,1,2,1,1,3)
            imie='imie2'
            nazwisko='nazwisko2'
            Flight.objects.create(airport = lotnisko, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)
            pass
        except ValidationError:
            self.fail("nie powinien zostac zwrocony blad a zostal")
