from django.db import models , transaction
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_fsm import FSMField, transition
from .choices import State , CustomerRespond
from inventory.models import InventoryItem 
from simple_history.models import HistoricalRecords


User = get_user_model()

history  = HistoricalRecords()
# Create your models here.
class StatusManager(models.Manager):
    def get_queryset(self):
        return(super().get_queryset().filter(status=Repair.Status.MBV))
    
class Client(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50 , blank=True)
    address = models.CharField(max_length=100 , blank=True)
    notes = models.TextField(blank=True)
    history
    #clien_for = models.TextChoices() should add this part - cleint is from who and should get choices from the user database and can add to the this
    def __str__(self):
        return f'{self.name}'
class Company(models.Model):
    client = models.ForeignKey(Client, on_delete=models.ProtectedError, blank=True,null=True, related_name='client')
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField(blank=True,)
    phonenumber = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=15)
    notes = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    contact_person = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    history
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('repairs:company_detail', args=[self.pk])
    
#Device informations
class Device(models.Model):
    brand = models.CharField(max_length=100, verbose_name='Brand')
    device_name = models.CharField(max_length=100 , verbose_name='Device name')
    part_number = models.CharField(max_length=100, verbose_name='Part number')
    serial_number = models.CharField(max_length=100, verbose_name='Serial number', unique=True)
    complain = models.TextField(blank=True, verbose_name='Customer complain', null=True)
    description = models.TextField(blank=True, verbose_name='Notes', null=True)
    shipped_from = models.TextField(blank=True , verbose_name='shipped from', null=True)
    postal_code = models.CharField(max_length=10, blank=True, verbose_name='Postal code', null=True)
    phone_numnber = models.CharField(blank=True, max_length=15 , verbose_name='Phone number', null=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    created_by = models.ForeignKey(User, on_delete=models.ProtectedError, verbose_name='Created by:')
    history
    
    def __str__(self):
        return f"{self.brand} {self.device_name} ({self.part_number}) Customer copmlain: {self.complain}".strip()
    
    def get_absolute_url(self):
        return True

class Repair(models.Model):
    job_number = models.PositiveIntegerField(blank=True, null=True ,unique=True, validators=[MaxValueValidator(999_999), MinValueValidator(100_000)], verbose_name='Job number')
    client = models.ForeignKey(Client, on_delete=models.ProtectedError, null=True, blank=True, related_name='Repairs',) # company.repairs.all()
    device = models.ForeignKey(Device, on_delete=models.ProtectedError,related_name='Device' ,null=True )
    created_by = models.ForeignKey(User, on_delete=models.ProtectedError, verbose_name='Created by:', related_name='createdby' ,null=True )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at',)
    
    state = FSMField(default=State.RECEIVED, protected=True)
    
    # data get at various steps
    assigned_to = models.ForeignKey(User, on_delete=models.ProtectedError, blank=True, null=True, verbose_name='Assigened to:')
    can_test = models.BooleanField(blank=True,verbose_name="Can device be tested", null=True)
    notes = models.TextField(blank=True, max_length=250, null=True )
    followed_up = models.CharField(max_length=250 ,null=True )
    video = models.FileField(upload_to='videos/',blank=True, verbose_name='upload video' ,null=True )
    parts_needs = models.ManyToManyField(InventoryItem, related_name='repairs' ,null=True )
    parts_total_price = models.PositiveIntegerField(verbose_name='At least total price of parts $:' ,blank=True ,null=True )
    customer_respond = models.CharField(max_length=15, choices=CustomerRespond, default=CustomerRespond.APPROVED, verbose_name='Customer respond' ,null=True )
    
    tracking_number = models.CharField(max_length=100, blank=True, verbose_name='Tracking number' ,null=True )
    updated_at = models.DateTimeField(auto_now=True ,null=True )
    history
    
    
    objects = models.Manager()
    MBV = StatusManager()
    
    def __str__(self):
        return f'Repair {self.job_number}  {self.device} for {self.company} [{self.state}]'
    
    @transition(field=state, source=State.RECEIVED, target=State.ASSIGNED )
    def move_to_assign(self):
        return 
    
    @transition(field=state, source=State.ASSIGNED, target=State.EVALUATING)
    def move_to_evaluating(self):
        return 
    
    @transition(field=state, source=State.VALIDATED, target=State.QUOTED)
    def move_to_qouting(self):
        return
    @transition(field=state, source=State.QUOTED, target=State.APPROVED)
    def move_to_approved(self):
        return
    @transition(field=state, source=[State.APPROVED, State.PART_ADDED], target=State.REPAIRING)
    def move_to_repairing(self):
        return
    @transition(field=state, source=State.REPAIRING, target=State.PART_ADDED)
    def move_to_part_adding(self):
        return
    @transition(field=state, source=State.REPAIRING, target=State.WAITING_FOR_PART)
    def move_to_waiting_part(self):
        return
    @transition(field=state, source=State.REPAIRING, target=State.REPAIRED)
    def move_to_repaired(self):
        return
    @transition(field=state, source=State.REPAIRED, target=State.READY_TO_SHIP )
    def move_to_read_to_ship(self):
        return
    @transition(field=state, source=State.READY_TO_SHIP, target=State.SHIPPED)
    def move_to_shipped(self):
        return
    @transition(field=state, source=State.SHIPPED, target=State.DONE)
    def move_to_done(self):
        return

    # class Meta:
        # ordering = ['']
        
        # indexes = [
        #     models.Index(fields=[''])
        # ]
        
    def __str__(self):
        return self.state
    
    
    #should add model manager later for just display customer and technician 
