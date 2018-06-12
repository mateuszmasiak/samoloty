# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Plane, Flight, Person, FlightPassenger, PlaneCrew
from django.contrib.auth.decorators import *
import datetime
from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from zad2.serializers import *
import requests


class Flightlist(TemplateView):
    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            flight_list = Flight.objects.all()
            return render(request,'flightlist.html',{'flight_list': flight_list})
        else:
            return render(request, 'startpage.html', context = None)


    def post(self,request, **kwargs):
        try:
            fr = datetime.datetime(int(request.POST.get('fry')), int(request.POST.get('frm')), int(request.POST.get('frd')), int(request.POST.get('frh')), int(request.POST.get('frmin')), int(request.POST.get('frsek')))
            until = datetime.datetime(int(request.POST.get('untily')), int(request.POST.get('untilm')), int(request.POST.get('untild')), int(request.POST.get('untilh')), int(request.POST.get('untilmin')),
            int(request.POST.get('untilsek')))
            flight_list = Flight.objects.filter(start_time__gte=fr, end_time__lte=until)
            return render(request,'flightlist.html',{'flight_list': flight_list})
        #try:
        #    fr = datetime.datetime(int(request.POST.get('fry')), int(request.POST.get('frm')), int(request.POST.get('frd')), int(request.POST.get('frh')), int(request.POST.get('frmin')), int(request.POST.get('frsek')))
        #    until = datetime.datetime(int(request.POST.get('untily')), int(request.POST.get('untilm')), int(request.POST.get('untild')), int(request.POST.get('untilh')), int(request.POST.get('untilmin')), int(request.POST.get('untilsek')))
        #    flight_list = Flight.objects.filter(start_time__gte=fr, end_time__lte=until)
        #    return render(request,'flightlist.html',{'flight_list': flight_list})
        except:
            flight_list = Flight.objects.all()
            return render(request,'flightlist.html',{'flight_list': flight_list})

@csrf_exempt
def planecrew_el(request,**kwargs):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        #r = requests.get('http://127.0.0.1:8000/planecrew/json/')#, auth=('user', 'pass'))
        #planes = Plane.objects.all()
        #serializer = PlaneSerializer(planes, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return render(request, 'plane_crew_el.html')

    elif request.method == 'POST':
        fname = request.POST.get('crew_first_name')
        print(fname)
    #    data = JSONParser().parse(request)
    #    serializer = FlightSerializer(data=data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return JsonResponse(serializer.data, status=201)
        #return JsonResponse(serializer.errors, status=400)

        return render(request, 'plane_crew_el.html')
@csrf_exempt
def planecrew_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if not request.user.is_authenticated:
        return render(request, 'startpage.html', context = None)
    if request.method == 'GET':
        print('planecrew get')
        #r = requests.get('http://127.0.0.1:8000/planecrew/json/')#, auth=('user', 'pass'))
        #planes = Plane.objects.all()
        #serializer = PlaneSerializer(planes, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return render(request, 'planecrew_list.html')

    elif request.method == 'POST':
        print('planecrew post json')
        try:
            data = JSONParser().parse(request)
            print(data)
            flight_id = data.get('id')
            fname = data.get('crew_first_name')
            lname = data.get('crew_last_name')

            fl= Flight.objects.get(id = int(flight_id))
            print(fl)
            start_time = fl.start_time
            end_time= fl.end_time
            flights = Flight.objects.filter(crew_last_name=lname, crew_first_name = fname)
            for f in flights:
                if (start_time > f.start_time and start_time<f.end_time) or (end_time > f.start_time and end_time<f.end_time):
                    return render(request, 'planecrewzbledem.html')
                elif start_time>f.start_time and end_time<f.end_time:
                    return render(request, 'planecrewzbledem.html')
            fl.crew_last_name=lname
            fl.crew_first_name=fname
            fl.save()

            return render(request, 'planecrew_list.html')
        except:
            return render(request, 'planecrewzbledem.html')




@csrf_exempt
def planecrew_list_json(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        print('planecrew get json')
        #planes = Plane.objects.all()
        #serializer = PlaneSerializer(planes, many=True)
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many = True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print('planecrew post json')
        try:
            data = JSONParser().parse(request)
            print(data)
            flight_id = data.get('id')
            fname = data.get('crew_first_name')
            lname = data.get('crew_last_name')

            fl= Flight.objects.get(id = int(flight_id))
            print(fl)
            start_time = fl.start_time
            end_time= fl.end_time
            flights = Flight.objects.filter(crew_first_name = fname,crew_last_name=lname)

            for f in flights:
                print('flight o imieniu: ')
                print(f)
                if (start_time > f.start_time and start_time < f.end_time) or (end_time>f.start_time and end_time<f.end_time):
                    return render(request, 'planecrewzbledem.html')
                if  (start_time < f.start_time and end_time>f.start_time):
                    return render(request, 'planecrewzbledem.html')

            fl.crew_last_name=lname
            fl.crew_first_name=fname
            fl.save()

            return render(request, 'planecrew_list.html')
        except:
            return render(request, 'planecrewzbledem.html')



#def plane_list(request):
#    qset_plane_list = Plane.objects.all()
class Flightview(TemplateView):
    def get(self,request, **kwargs):
        if request.user.is_authenticated:
            invalid = False
            flight = Flight.objects.get(id = self.kwargs['fid'])
            flightpassengers = FlightPassenger.objects.filter(flight_id = flight.id)
            persons = {}
            for fp in flightpassengers:
                for p in Person.objects.all():
                    if p == fp.person_id:
                        print(p.first_name)
                        print(p.last_name)
                        persons[p] = fp.places_purchased
            return render(request, 'flight.html', {'flight': flight, 'persons':persons, 'invalid': invalid})
        else:
            return render(request, 'startpage.html', context = None)

    def post(self, request, **kwargs):
        try:
            invalid = False
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            if not Person.objects.filter(first_name = fname, last_name = lname).exists():
                print('osoba nie istniala, tworze nowa')
                person = Person.objects.create(first_name = fname, last_name = lname)
            else:
                print('osoba istaniala, aktualizuje stara')
                person = Person.objects.get(first_name = fname, last_name = lname)

            flight = Flight.objects.get(id = self.kwargs['fid'])
            y = request.POST.get('plac')
            number_to_purchase = int(y)
            print('kupuje '+y+' miejsc ')
            total_places = flight.plane.places
            new_purchased = number_to_purchase
            flightpassengers = FlightPassenger.objects.filter(flight_id = flight.id)
            for fp in flightpassengers:
                if fp.person_id != person:
                    total_places -=fp.places_purchased
                else:
                    new_purchased+=fp.places_purchased

            if total_places >= new_purchased and FlightPassenger.objects.filter(flight_id = flight, person_id =person).exists():
                print(' wystarczajaco wolnych miejsc i zlaczenie istnieje, tylko ja aktualizuej')
                print('wolnych miejsc bylo:' + str(total_places))
                fp1 = FlightPassenger.objects.get(flight_id=flight,person_id=person)
                print('new purchased: '+str(new_purchased))
                fp1.places_purchased = new_purchased
                fp1.save()
            elif total_places >= new_purchased:
                print('wystarczy wolnych miejsc ale zlaczenie nie istnieje wiec je tworze')
                print('wolnych miejsc bylo:' + str(total_places))
                f = FlightPassenger.objects.create(places_purchased = new_purchased,
                flight_id = flight, person_id = person)
            else:
                print('brak miejsc')
                invalid = True

#wyswietlanie po zmianie
            persons = {}
            flightpassengers = FlightPassenger.objects.filter(flight_id = flight.id)

            for fp in flightpassengers:
                for p in Person.objects.all():
                    if p == fp.person_id:
                        persons[p] = fp.places_purchased

            return render(request, 'flight.html', {'flight': flight, 'persons':persons , 'invalid': invalid})

        except:
            flight = Flight.objects.get(id = self.kwargs['fid'])
            flightpassengers = FlightPassenger.objects.filter(flight_id = flight.id)
            persons = {}
            for fp in flightpassengers:
                for p in Person.objects.all():
                    if p == fp.person_id:
                        persons[p] = fp.places_purchased
            return render(request, 'flight.html', {'flight': flight, 'persons':persons, 'invalid' : False})



class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'startpage.html', context = None)

class Loggout(TemplateView):
    def get(self,request,**kwargs):
        if request.user.is_authenticated:
            logout(request)
            return render(request, 'logout.html', context = None)
        else:
            return render(request, 'startpage.html', context = None)
