from django.urls import path,include
from .views  import CustomUserCreate,BlackListTokenView,RetriveUserView,UserDetailPage,CreateUser,EditUser
from .views import AdminUserDetail,DeleteUser

from rest_framework.routers import SimpleRouter
from rest_framework import routers
#api end points
app_name='api_view'
router=routers.SimpleRouter()
router.register('',UserDetailPage,basename="new")
urlpatterns=[
   path('register/',CustomUserCreate.as_view(),name='create_user'),
   path('logout/blacklist/',BlackListTokenView.as_view(),name='blacklist'),
   path('authuser/',RetriveUserView.as_view(),name="retrive_user"),
   #crud urls
   path('admin/create/',CreateUser.as_view()),
   path('admin/edit/userdetail/<int:pk>/',AdminUserDetail.as_view()),
   path('admin/edit/<int:pk>/',EditUser.as_view()),
   path('admin/delete/<int:pk>/',DeleteUser.as_view()),


]

urlpatterns +=router.urls