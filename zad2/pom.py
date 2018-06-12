def clean1(self, date):
    for f in Flight.objects.filter(plane = self.plane):
        if date >= f.start_time and date <= f.end_time:
            raise ValidationError(_('Two flights at the same time'))

class PlaneCrew(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Plane(models.Model):
    rejestration_number = models.CharField(max_length=30)
    places = models.IntegerField()
# TODO NIE DA SIE USUNAC TYLKO ZASTAPIC + nie da sie dwoch lotow w tym samym czasie
    #crew = models.ForeignKey(PlaneCrew, on_delete=models.CASCADE)
    def __str__(self):
        return self.rejestration_number
    def add(self):
        self.save()





class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Flight(models.Model):
    airport = models.CharField(max_length=30)
    start_time = models.DateTimeField(validators=[clean1])
    end_time = models.DateTimeField(validators=[clean1])
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

    def clean(self):
        for f in Flight.objects.filter(plane = self.plane):
            if (self.start_time >= f.start_time and self.start_time <= f.end_time) or (self.end_time>=f.start_time and self.end_time<=f.end_time):
                raise ValidationError(_('Two flights at the same time'))
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














xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        myFunction(myArr);
    }
};
xmlhttp.open("POST", url, true);
xmlhttp.send(mdata);
