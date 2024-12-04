from rest_framework import serializers
from .models import usersDetail
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = usersDetail
        fields = '__all__'
