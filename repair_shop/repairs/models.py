from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
class StatusManager(models.Manager):
    def get_queryset(self):
        return(super().get_queryset().filter(status=RepairJobs.Status.MBV))
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phonenumber = models.CharField(max_length=20, blank=True)
    postal_code = models.CharField(max_length=15)
    notes = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    contact_person = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Client(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, blank=True,null=True, related_name='clients')
    name = models.CharField(max_length=20)
    phone_numeber = models.CharField(max_length=20)
    email = models.EmailField(max_length=50 , blank=True)
    address = models.CharField(max_length=100 , blank=True)
    notes = models.TextField()
    #clien_for = models.TextChoices() should add this part - cleint is from who and should get choices from the user database and can add to the this
    def __str__(self):
        if self.company:
            return f'{self.name} from {self.company}'
        return f'{self.name}'


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
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name='Repairs') # company.repairs.all()
    job_number = models.PositiveIntegerField(unique=True, )
    device_name = models.CharField(max_length=250, verbose_name="Device brand:")
    notes = models.CharField(max_length=250,)
    device_part_number = models.PositiveIntegerField(
        validators=[MaxValueValidator(999_999), MinValueValidator(100_000)],
        verbose_name="Device Part number")
    can_test = models.BooleanField(verbose_name="can device be tested",)
    assigned_to = models.CharField(max_length=250,)
    date = models.DateField(auto_now_add=True, verbose_name='date created',)
    status = models.CharField(max_length=10,
                                choices=Status,default=Status.MBV)
    followed_up = models.CharField(max_length=250)
    
    video = models.FileField(upload_to='videos/',blank=True,
                            verbose_name='upload video',)
    
    parts_needs = models.CharField(max_length=250, blank=True)
    
    brand = models.CharField(max_length=250, default='not known')
    
    # from recieving to shipping between (shipper , customer service , repair technicain)
    date_recieved = models.DateField(auto_now_add=True)
    date_assigned = models.DateField(auto_now_add=True)
    date_validate = models.DateField(auto_now_add=True, blank=True)
    date_qoute = models.DateField(auto_now_add=True, blank=True)
    date_accept = models.DateField(auto_now_add=True, blank=True)
    date_working_on = models.DateField(auto_now_add=True)
    date_repaired = models.DateField(auto_now_add=True, blank=True)
    date_confirmed = models.DateField(auto_now_add=True, blank=True)
    date_shipped = models.DateField(auto_now_add=True, blank=True)
    
    
    objects = models.Manager()
    MBV = StatusManager()
    class Meta:
        ordering = ['-date','-status']
        
        indexes = [
            models.Index(fields=['-date'])
        ]
        
    def __str__(self):
        return self.device_name
    
    
    #should add model manager later for just display customer and technician 
