from rest_framework import serializers

from django.contrib.auth.models import Group

class GroupSerialzier(serializers.ModelSerializer):

    class Meta:
        model=Group
        fields='__all__'