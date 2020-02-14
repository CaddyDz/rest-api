from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
                'id', 'username', 'is_superuser', 'email', 'first_name', 'last_name',
                'reset_token', 'remember_at', 'email_verified_at', 'clients_table', 
                'events_table', 'attendees_table',
]
