from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def architecture(request):
    return render(request,'catalogue/ArchiCatalogue.html')
