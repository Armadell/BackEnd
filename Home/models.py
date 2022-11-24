


from django.db import models
from django.contrib.auth.models  import User
# Create your models here.


class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_picture")
    profile_picture = models.ImageField(blank=True, upload_to="userprofile", null=True,default="/default/man-156584_960_720.webp")
