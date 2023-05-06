from rest_framework import serializers
from .models import *


class POSTSerializer(serializers.ModelSerializer):

    class Meta:
        model=Post
        # fileds=('id','name' , 'email', 'title' , 'tags' , 'description')
        fields = '__all__'


    # email = serializers.EmailField()
    # content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField()