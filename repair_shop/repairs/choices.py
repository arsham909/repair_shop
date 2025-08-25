from django.db import models

class State(models.TextChoices):
    RECEIVED = "received", "Received"
    VALIDATED = "validated", "Validated"
    ASSIGNED = "assigned", "Assigned"
    EVALUATING = "evaluating", "Evaluating"
    QUOTED = "quoted", "Quoted"
    APPROVED = "approved", "Approved"
    REPAIRING = "repairing", "Repairing"
    REPAIRED = 'repaired', 'Repaired'
    WAITING_FOR_PART = "waiting_for_part", "Waiting for part"
    PART_ADDED = 'part_added', 'Part added'
    SHIPPED = "shipped", "Shipped"
    REJECTED = "rejected", "Rejected"
    CANCELLED = "cancelled", "Cancelled"
    SCRAP = 'scrap', 'Scrapped'
    READY_TO_SHIP = 'ready_to_ship' , 'Ready to ship'
    DONE = 'done', 'Done'
    
class CustomerRespond(models.TextChoices):
    APPROVED = 'approved', "Approved"
    REJECTED = 'rejected', "Rejected"