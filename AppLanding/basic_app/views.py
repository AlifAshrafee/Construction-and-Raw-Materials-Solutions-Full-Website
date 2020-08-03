from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
from basic_app.models import vendorProfile,companyProduct
from django.db import connection
from django.conf import settings

import re
import cx_Oracle

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from collections import namedtuple



# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
    # Log out the user
    session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)

    with connection.cursor() as cursor:
        cursor.callproc('user_logout',[session_key])
    request.session.flush()
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered=False
    if request.method == 'POST':

        user_form=UserForm(data=request.POST)
        profile_form= UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            profile.save()
            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'basic_app/SignUp_FormValidation.html',{'user_form':user_form,
                                                        'profile_form':profile_form,
                                                        'registered':registered})
def user_login(request):

    if request.method == 'POST':

        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        print(username)
        print(password)
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("<h1>Invalid login details supplied.</h1>")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/index.html', {})


def search_product(request):
    if request.method=='POST':
        search=request.POST['search']
        if search:
            with connection.cursor() as cursor:
                    #cursor.execute("select company_name,category,product_name,product_price,user_rating from basic_app_vendorProfile inner join basic_app_companyProduct on basic_app_vendorProfile.ID=basic_app_companyProduct.vendor_ID_ID where upper(category) like upper('"+search+"%') OR upper(product_name) like upper('"+search+"%') OR upper(company_name) like upper('"+search+"%') ")
                    l_cur=cx_Oracle.Cursor(cx_Oracle.connect("hr/hr@(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521))"
                    "(CONNECT_DATA =(SERVER = DEDICATED)(SERVICE_NAME = system)))"))
                    cursor.callproc('search_result',[search,l_cur])
                    #cols=[col[0] for col in l_cur]
                    #rows=[dict(zip(cols,rows)) for rows in l_cur.fetchall()]
                    #rows=list(l_cur.fetchall())
                    columns=['Company Name','Company Product','Category','Price','Rating']
                    rows=[dict(zip(columns,rows)) for rows in l_cur.fetchall()]
                    print(rows)
            return render(request,'basic_app/search_result.html',{'result':rows,'columns':columns})
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'basic_app/index.html')
