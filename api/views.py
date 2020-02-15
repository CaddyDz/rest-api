from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('-date_joined')
    serializer_class = PersonSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
