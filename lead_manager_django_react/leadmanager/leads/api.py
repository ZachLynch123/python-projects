from leads.models import Lead
from rest_framework import viewsets, permissions
from serializers import LeadSerializer

# Lead ViewSet
# viewset allows us to create CRUD API without having to specify explicit method for functionality

class LeadViewSet(viewsets.ModelViewSet): 
    queryset = Lead.objects.all()
    permission_classes= [
        # Change later
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer