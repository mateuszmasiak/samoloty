for x in range(0, 50):
    napis = "Samolot" + str(x)
    Plane.objects.create(rejestration_number = napis, places = 20 +x)



for pl in Plane.objects.all():
    for x in range(0, 50):
        napis = "lotnisko" + str(x)
        start = datetime(2010+x,(1+x)%10+1,(1+x)%10+1, (1+x)%22+1,(1+x),(3+x))
        koniec = datetime(2010+x,(1+x)%10+2,(1+x)%10+2, (1+x)%22+2,(1+x),(3+x))
        imie = "imie"+str(x)
        nazwisko= "nazwisko" + str(x)
        Flight.objects.create(airport = napis, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)

#logowanie tylko dla zalogowanego uzytkownika
#komunikat o bledzie

lotnisko = 'l'
start = datetime(2009,1,1,1,1,3)
koniec = datetime(2011,1,1,1,1,3)
imie='imie'
nazwisko='nazwisko'
pl=Plane.objects.get(id=1)
Flight.objects.create(airport = lotnisko, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)

lotnisko = 'l'
start = datetime(2010,1,1,1,1,3)
koniec = datetime(2010,1,2,1,1,3)
imie='imie'
nazwisko='nazwisko'
pl=Plane.objects.get(id=1)
Flight.objects.create(airport = lotnisko, start_time = start, end_time = koniec, plane = pl, crew_last_name = nazwisko, crew_first_name = imie)



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



#samolot nie moze wykonywac dwoch lotow w tym samym momencie w modelu
