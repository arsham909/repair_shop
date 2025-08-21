from django.db import models
from django.urls import reverse
from .choices import Category
from simple_history.models import HistoricalRecords

# Create your models here.
class Stustmanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    def quantity (self):
        return super().get_queryset().filter(quantity__lt = 10)
    

class InventoryItem(models.Model):

    name = models.CharField(max_length=250)
    part_number = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField()
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=250)
    category = models.CharField(max_length=50, choices=Category, default=Category.RESISTORS)
    is_active = models.BooleanField(default=True)
    trigger = models.PositiveIntegerField( default=0)
    
    history = HistoricalRecords()
    # add less than this number give the technician warning
    objects = models.Manager()
    
    to_buy = Stustmanager()
    
    def get_absolute_url(self):
        return reverse('inventory:component_detail', args=[self.pk])
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name