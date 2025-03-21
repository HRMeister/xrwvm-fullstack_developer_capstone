# Uncomment the following imports before adding the Model code

from django.db import models
#from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    num = models.IntegerField()

    def __str__(self):
        return str(self.num) + "." + self.name


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(default=1)
    CAR_TYPES = [
        ('SEDAN','Sedan'), 
        ('SUV', 'SUV'), 
        ('WAGON', 'Wagon')
        ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default = 'SUV')
    year = models.IntegerField(default=2024,
        validators = [
           MaxValueValidator(2024), 
           MinValueValidator(2015)
        ])
    COLORS = [
        ('red', 'RED'),
        ('black', 'BLACK'),
        ('white', 'WHITE'),
        ('blue', 'BLUE')
    ]
    color = models.CharField(max_length=10, choices=COLORS, default='white')

    def __str__(self):
        return self.name
