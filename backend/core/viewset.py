from rest_framework import viewsets
from django.contrib.auth.models import User

from .models import *
from .serializers import *


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field  = 'pk'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer