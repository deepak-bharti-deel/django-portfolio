from django.db import models

# Create your models here.

class Booking(models.Model):
    last_booked_seat_no = models.IntegerField()

class Seat(models.Model):
    status = models.CharField(max_length=1) # 'a' - available, 'b' - booked
    seat_number = models.IntegerField() # 1,2, ..., 80
