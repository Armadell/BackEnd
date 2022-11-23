from rest_framework import serializers
from django.contrib.auth.models import User
from Home.models import UserProfile
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
       
    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        obj=User.objects.all()
      
        return instance
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email']
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"