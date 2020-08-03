from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def architecture(request):
    return render(request,'catalogue/ArchiCatalogue.html')

def complete(request):
    return render(request,'catalogue/CompleteCatalogue.html')

def construction(request):
    return render(request,'catalogue/ConstructionCatalogue.html')

def engineering(request):
    return render(request,'catalogue/EngCatalogue.html')

def rawMaterials(request):
    return render(request,'catalogue/RawMaterialsCatalogue.html')
