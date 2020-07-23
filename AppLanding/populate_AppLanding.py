import os
# Configure settings for project
# Need to run this before calling models from application!
from django.db import connection
import cx_Oracle
import re
os.environ.setdefault('DJANGO_SETTINGS_MODULE','AppLanding.settings')

import django
# Import settings
django.setup()

import random
from basic_app.models import vendorProfile,companyProduct
from faker import Faker

fakegen = Faker()
categories = ['Architecture','Engineering','Construction','RawMaterials','Complete']
construction=['piling','fitting','transportation','labor']
raw_material=['cement','brick','rod','wood','concrete','bamboo','metal','glass','ceramics']
architecture=['interior','exterior']
engineering=['civil','structural','mechanical','electrical','plumbing']

def add_vendor(num,fake_name):
    type=random.choice(categories)
    with connection.cursor() as cursor:
        vendor_id=cursor.var(int).var
        ID = cursor.var(int).var
        cursor.callproc('insert_vendorprofile',[ID,type,fake_name,num,vendor_id])
        #vendor = vendorProfile.objects.get_or_create(category=type,company_name=fake_name,user_rating=num)[0]
        v_id=vendor_id.getvalue()
        vendor_info=[v_id,type]
    return vendor_info



def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.company()
        num=random.randint(2,10)
        price=random.randint(500,3000)

        v_info = add_vendor(num,fake_name)
        v_id=v_info[0]
        top=v_info[1]
        if(top=="Architecture"):
            prod=random.choice(architecture)
        elif(top=="Construction"):
            prod=random.choice(construction)
        elif(top=="RawMaterials"):
            prod=random.choice(raw_material)
        elif(top=="Engineering"):
            prod=random.choice(engineering)
        elif(top=="Complete"):
            prod= 'null'
        with connection.cursor() as cursor:
            cursor.callproc('insert_product',[v_id,prod,price])
        #product = companyProduct.objects.get_or_create(vendor_ID=top,product_name=prod,product_price=price)[0]

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(1)
    print('Populating Complete')
