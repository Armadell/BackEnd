from rest_framework import serializers
from django.contrib.auth.models import User
from Home.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
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
        fields=["username","email"]

       
class UserDetailSerializer(serializers.ModelSerializer):
     user=UserSerializer()
     class Meta:
        model=UserProfile
        fields=['user','profile_picture']




