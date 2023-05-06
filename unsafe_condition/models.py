from django.db import models

# Create your models here.

class UnsafeCondition(models.Model):
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='unsafe_condition_photos/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.description[:20]}... at {self.location}'