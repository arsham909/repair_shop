from django.db import models

# Create your models here.
class Stustmanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    def quantity (self):
        return super().get_queryset().filter(quantity__lt = 10)

class InventoryItem(models.Model):
    
    name = models.CharField(max_length=250)
    part_number = models.CharField(max_length=250)
    quantity = models.IntegerField()
    note = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    
    objects = models.Manager()
    
    to_buy = Stustmanager()
    
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name