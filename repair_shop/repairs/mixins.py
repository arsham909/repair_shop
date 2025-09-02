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