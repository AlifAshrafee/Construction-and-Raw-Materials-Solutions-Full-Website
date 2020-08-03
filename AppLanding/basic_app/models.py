# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db import connection

# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User)
    contact_number=models.CharField(max_length=15)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

class vendorProfile(models.Model):
    company_name=models.CharField(max_length=264)
    category=models.CharField(max_length=264)
    user_rating=models.IntegerField()

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.company_name

class companyProduct(models.Model):
    vendor_ID=models.ForeignKey(vendorProfile)
    product_name=models.CharField(max_length=30,null=True)
    product_price=models.IntegerField()

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.product_name
