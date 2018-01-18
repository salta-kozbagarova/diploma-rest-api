from auction.bargains.models import Bargain, BargainType
from rest_framework import generics
from auction.bargains.serializers import BargainSerializer, BargainTypeSerializer
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
# Create your views here.

class BargainViewSet(viewsets.ModelViewSet):

    queryset = Bargain.objects.all()
    serializer_class = BargainSerializer

class BargainTypeViewSet(viewsets.ModelViewSet):

    queryset = BargainType.objects.all()
    serializer_class = BargainTypeSerializer