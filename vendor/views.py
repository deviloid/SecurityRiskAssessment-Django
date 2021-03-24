from django.shortcuts import render

# Create your views here.

def createVendor(request):
    return render(request, 'vendor/createVendor.html')

def vendorRoleError(request):
    context={'val':True}
    return render(request, 'vendor/VendorRoleError.html', context)