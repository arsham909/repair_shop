from django.db.models import Q

class ClientSearchMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('SearchClients', '')
        
        if query :
            return queryset.filter(
                Q(name__icontains=query)|
                Q(phone_number__icontains=query)|
                Q(email__icontains=query)|
                Q(address__icontains=query)
            )
        return queryset
    
class RepairSearchMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('SearchRepairs', '')
        
        if query:
        # The search lookups must be on the related model's fields
            return queryset.filter(
                Q(job_number__icontains=query) |
                Q(device__brand__icontains=query)|
                Q(device__device_name__icontains=query)|
                Q(device__serial_number__icontains=query)|
                Q(device__part_number__icontains=query)|
                Q(assigned_to__username__icontains=query)|
                Q(state__icontains=query)
            )
        return queryset
    
