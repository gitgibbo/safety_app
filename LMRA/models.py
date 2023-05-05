from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class LMRA(models.Model):
    """Basic LMRA model"""
    date_added = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.location
    
class Hazard(models.Model):
    """basic hazard model"""
    hazard = models.CharField(max_length=50)
    description = models.TextField()
    likelihood = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    severity = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    lmra = models.ForeignKey(LMRA, on_delete=models.CASCADE)

    def __str__(self):
        return self.hazard