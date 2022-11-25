from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from Home.models import User,UserProfile
from .serializers import RegisterUserSerializer,UserSerializer,UserDetailSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import permissions
from rest_framework import views,generics
from rest_framework.response import Response
from django.contrib.auth import login

from . import serializers
from django.shortcuts import get_object_or_404
class CustomUserCreate(APIView):
    permission_classes=[AllowAny]
    
    def post(self,request):
        print(request.user)
        reg_serializer=RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            user=reg_serializer.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_404_NOT_FOUND)
class BlackListTokenView(APIView):
    permission_classes=[AllowAny]
 
    def post(self,request):
    
        try:
            refresh_token=request.data["refresh_token"]
          
            token=RefreshToken(refresh_token)
          
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print("step1")
            return Response(status=status.HTTP_400_BAD_REQUEST)
class RetriveUserView(APIView):
     permission_classes = [IsAuthenticated]
     def get(self,request):
         
         profile=request.user.profile_picture
        #  user=UserSerializer(user)
         user=UserDetailSerializer(profile,many=True)
         
         print(user.data)
         return Response(user.data,status=status.HTTP_200_OK)
class UserDetailPage(viewsets.ViewSet):
    permission_classes=[IsAdminUser]
    queryset=User.objects.all()
    def list(self,request):
        serializer_class=UserSerializer(self.queryset,many=True)
        return Response(serializer_class.data)
    def retrieve(self,request,pk=None):
        new_query=get_object_or_404(self.queryset,pk=pk)
        serializer_class=UserSerializer(new_query)
        return Response(serializer_class.data)
class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        login(request, user)
        
       

        return Response(None, status=status.HTTP_202_ACCEPTED)
class ProfileView(generics.ListCreateAPIView):
   
    queryset=UserProfile.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [permissions.IsAdminUser]
   

    def get_object(self):
        return self.request.user
#crud operations in front end
class CreateUser(generics.CreateAPIView):
    permission_classes=[permissions.IsAdminUser]
    queryset=User.objects.all()
    serializer_class=UserSerializer
class AdminUserDetail(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAdminUser]
    queryset=User.objects.all()
    serializer_class=UserSerializer
class EditUser(generics.UpdateAPIView):
    permission_classes=[permissions.IsAdminUser]
    queryset=User.objects.all()
    serializer_class=UserSerializer
class DeleteUser(generics.RetrieveDestroyAPIView):
    permission_classes=[permissions.IsAdminUser]
    queryset=User.objects.all()
    serializer_class=UserSerializer

    


    

