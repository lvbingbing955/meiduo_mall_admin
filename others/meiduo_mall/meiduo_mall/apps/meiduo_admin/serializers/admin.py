from rest_framework import serializers
from users.models import User

class AdminSerialzier(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'
        extra_kwargs={
            'password':{
                'write_only':True
            }
        }




    def create(self, validated_data):
        # 添加字段
        validated_data['is_staff']=True
        admin=super().create(validated_data)

        # 密码
        password=validated_data['password']
        admin.set_password(password)
        admin.save()


        return admin


    def update(self, instance, validated_data):

        admin = super().update(instance,validated_data)

        # 密码
        password = validated_data['password']
        admin.set_password(password)
        admin.save()


        return admin