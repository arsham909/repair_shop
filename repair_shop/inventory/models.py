from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    
    name = models.CharField(max_length=250)
    part_number = models.CharField(max_length=250)
    quantity = models.IntegerField()
    note = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name