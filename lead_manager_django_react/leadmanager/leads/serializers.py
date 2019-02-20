from rest_framework import serializers
from leads.models import Lead

# Lead Serializer

## Takes data from database and converts it into JSON

class LeadSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Lead
        fields = '__all__'