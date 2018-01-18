from auction.categories.models import Category
from rest_framework import generics
from auction.categories.serializers import CategorySerializer
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer