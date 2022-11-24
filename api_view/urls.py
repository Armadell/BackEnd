from django.urls import path,include
from .views  import CustomUserCreate,BlackListTokenView,RetriveUserView,UserDetailPage
from rest_framework.routers import SimpleRouter
from rest_framework import routers
#api end points
app_name='api_view'
router=routers.SimpleRouter()
router.register('',UserDetailPage,basename="new")
urlpatterns=[
   path('register/',CustomUserCreate.as_view(),name='create_user'),
   path('logout/blacklist/',BlackListTokenView.as_view(),name='blacklist'),
   path('authuser/',RetriveUserView.as_view(),name="retrive_user")

]

urlpatterns +=router.urls