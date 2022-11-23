from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from Home.models import User,UserProfile
from .serializers import RegisterUserSerializer,UserSerializer,UserDetailSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
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
         user=request.user
         user=UserSerializer(user)
         print(user.data)
         return Response(user.data,status=status.HTTP_200_OK)
class UserDetailPage(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]
    queryset=User.objects.all()
    def list(self,request):
        serializer_class=UserDetailSerializer(self.queryset,many=True)
        return Response(serializer_class.data)
    def retrieve(self,request,pk=None):
        new_query=get_object_or_404(self.queryset,pk=pk)
        serializer_class=UserDetailSerializer(new_query)
        return Response(serializer_class.data)
        
   
