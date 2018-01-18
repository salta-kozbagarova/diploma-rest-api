from rest_framework import serializers
from django.contrib.auth.models import User
from auction.categories.models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'image',
                  'link', 'parent_id')