from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
class RepairJobs(models.Model):
    class Status(models.TextChoices):
        MBV = 'MBV', 'Must be validate'
        Validated = 'Val', 'Validation'
        Quoted = 'Quoted', 'Quoted'
        WFP = 'WFP', 'Waiting for parts'
        Done = 'Done', 'Done'
        RTS = 'RTS' , 'Ready To Ship'
        Shipped = 'Shipped', 'Shipped'
        Scrap = 'Scrap', 'Scrapped'
    
    job_number = models.IntegerField(unique=True, help_text="Enter the job number:")
    device_name = models.CharField(max_length=250, verbose_name="Device brand:")
    notes = models.CharField(max_length=250, help_text="notes")
    device_part_number = models.IntegerField(
        validators=[MaxValueValidator(999_999), MinValueValidator(100_000)],
        help_text="Device Part number",
        verbose_name="Device Part number",
    )
    can_test = models.BooleanField(verbose_name="can device be tested",)
    assigned_to = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True, verbose_name='date created',)
    status = models.CharField(max_length=10,
                                choices=Status,default=Status.MBV)
    followed_up = models.CharField(max_length=250)
    
    video = models.FileField(upload_to='videos/',blank=True,
                            verbose_name='upload video',help_text='upload ur video here')
    
    parts_needs = models.CharField(max_length=250, help_text='parts needed ', blank=True)
    
    brand = models.CharField(max_length=250, default='not known')
    
    class Meta:
        ordering = ['-date','-status']
        
        indexes = [
            models.Index(fields=['-date'])
        ]
        
    def __str__(self):
        return self.device_name
    
    
    
    #should add model manager later for just display customer and technician 
    