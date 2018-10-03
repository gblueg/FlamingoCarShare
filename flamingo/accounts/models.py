from django.db import models
from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
from django.urls import reverse

class Car(models.Model):
    car_id = models.IntegerField("Car", primary_key=True)
    car_name = models.CharField("Model", max_length=50, null=True, blank=True)
    #image = models.ImageField(upload_to='car_images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField("Price per day", null=True, blank=True)
    lat = models.CharField(max_length=50, null=True, blank=True)
    lng = models.CharField(max_length=50, null=True, blank=True)
    #CHOICES = ((True, 'Yes'),(False, 'No') )
    #available = models.BooleanField("Is Available", choices = CHOICES, default=True)
    icon = models.IntegerField("Car Image Icon", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk': self.pk})
    def __str__(self):
        return self.car_name

class Booking(models.Model):
    booking_id = models.AutoField("Booking", primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Customer")
    book_start_date = models.DateField("Start date", null=True, blank=True)
    book_end_date = models.DateField("End date", null=True, blank=True)
    start_time = models.TimeField("Start time", null=True, blank=True)
    end_time = models.TimeField("End time", null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Cars")
    #available = models.ForeignKey(Available, on_delete=models.CASCADE, default=False, verbose_name="Car Available")

    def get_absolute_url(self):
        return reverse('booking-details', kwargs={'pk': self.pk})
    def __str__(self):
        return str(self.customer)
