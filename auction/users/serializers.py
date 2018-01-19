from rest_framework import serializers
from auction.users.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'phone', 'is_staff', 'bargains_bargaintype_related')