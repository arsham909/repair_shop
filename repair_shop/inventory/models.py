from django.db import models

# Create your models here.
class Stustmanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    def quantity (self):
        return super().get_queryset().filter(quantity__lt = 10)
    

class InventoryItem(models.Model):
    class Category(models.TextChoices):
        RESISTORS = 'RES', 'Resistors'
        CAPACITORS = 'CAP', 'Capacitors'
        INDUCTORS = 'IND', 'Inductors'
        DIODES = 'DIO', 'Diodes'
        LEDS = 'LED', 'LEDs'
        TRANSISTORS = 'TRA', 'Transistors'
        FETS = 'FET', 'FETs & MOSFETs'
        THYRISTORS = 'SCR', 'Thyristors & SCRs'
        ICS = 'INT', 'Integrated Circuits'
        MICROCONTROLLERS = 'MIC', 'Microcontrollers'
        MEMORY = 'MEM', 'Memory'
        SENSORS = 'SEN', 'Sensors'
        CRYSTALS = 'CRY', 'Crystals & Oscillators'
        RELAYS = 'REL', 'Relays'
        SWITCHES = 'SWI', 'Switches'
        BUTTONS = 'BUT', 'Buttons'
        POTENTIOMETERS = 'POT', 'Potentiometers & Trimmers'
        CONNECTORS = 'CON', 'Connectors'
        TERMINALS = 'TER', 'Terminals'
        HEADERS = 'HEA', 'Headers & Sockets'
        FUSES = 'FUS', 'Fuses'
        BREAKERS = 'BRE', 'Circuit Breakers'
        TRANSFORMERS = 'TRANSF', 'Transformers'
        REGULATORS = 'REG', 'Voltage Regulators'
        DISPLAYS = 'DIS', 'Displays'
        POWER_SUPPLIES = 'POW', 'Power Supplies'
        BATTERIES = 'BAT', 'Batteries'
        MOTORS = 'MOT', 'Motors'
        FANS = 'FAN', 'Fans & Heat Sinks'
        FILTERS = 'FIL', 'Filters'
        ANTENNAS = 'ANT', 'Antennas'
        MODULES = 'MOD', 'Modules'
        PCBS = 'PCB', 'PCB & Prototyping'
        TOOLS = 'TOO', 'Tools & Accessories'
        WIRES = 'WIR', 'Wires & Cables'
        HARDWARE = 'HAR', 'Hardware'
        MECHANICAL = 'MEC', 'Mechanical Parts'
        LABELS = 'LAB', 'Labels & Markers'
        OTHER = 'OTH', 'Other'
    
    name = models.CharField(max_length=250)
    part_number = models.CharField(max_length=250)
    quantity = models.IntegerField()
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=250)
    category = models.CharField(max_length=50, choices=Category, default=Category.RESISTORS)
    
    objects = models.Manager()
    
    to_buy = Stustmanager()
    
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name