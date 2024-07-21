from .models import Person,Product,Orders,Sales_Team
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Person
        fields = ['url','id_no','fname','lname','email','address']