from django.db import models # type: ignore
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TripBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    destination = models.CharField(max_length=100)
    travel_date = models.CharField(max_length=100)  # storing as text
    people = models.CharField(max_length=100)       # storing as text
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.destination}"
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
