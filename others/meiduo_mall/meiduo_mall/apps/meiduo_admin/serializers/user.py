from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
        用户序列化器
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email','password')

        extra_kwargs={
            'password':
                {
                    'write_only':True,
                    'max_length':20,
                    'min_length':8
                },
            'username':{
                'max_length': 20,
                'min_length': 5
            }
        }

    def create(self, validated_data):

       user = User.objects.create_user(**validated_data)

       return user


