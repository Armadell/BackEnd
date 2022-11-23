from django.urls import path
from .views  import CustomUserCreate,BlackListTokenView,RetriveUserView,UserDetailPage
from rest_framework.routers import DefaultRouter
#api end points
app_name='api_view'

urlpatterns=[
   path('register/',CustomUserCreate.as_view(),name='create_user'),
   path('logout/blacklist/',BlackListTokenView.as_view(),name='blacklist'),
   path('authuser/',RetriveUserView.as_view(),name="retrive_user")

]
router=DefaultRouter()