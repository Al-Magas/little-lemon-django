from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.PositiveIntegerField()
    comment = models.TextField(max_length=1000, blank=True)

    date = models.DateField(default=date.today)
    creneau = models.CharField(
        max_length=50,
        choices=[
            ('08:00-10:00', '08:00 - 10:00'),
            ('10:00-12:00', '10:00 - 12:00'),
            ('14:00-16:00', '14:00 - 16:00'),
            ('16:00-18:00', '16:00 - 18:00'),
        ],
    )

    class Meta:
        unique_together = ('date', 'creneau')
        ordering = ['date', 'creneau']

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.date} | {self.creneau}"


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    menu_item_description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)

    def __str__(self):
        return self.name
