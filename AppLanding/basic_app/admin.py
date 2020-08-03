from django.contrib import admin

# Register your models here.
from django.contrib import admin
from basic_app.models import UserProfileInfo,User,vendorProfile,companyProduct

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(vendorProfile)
admin.site.register(companyProduct)
