from django.db import reset_queries
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import Account
from vendor.models import UserVendor
from .forms import DepartmentSignUpForm, VendorSignUpForm

# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user == None:
        return redirect('login')
    if request.user.is_uservendor:
        user_v = UserVendor.objects.get(user_id=request.user.id).userType_id
        if user_v != 3:
            return redirect('vendorRoleError')
    # context = {'user':request.user}
    # user_v = UserVendor.objects.get(user_id=request.user.id)
    # e = UserVendor(user=request.user, userType_id=3)
    # e.save()
    # print(user_v)
    # print(request.user.id)
    return render(request, 'accounts/index.html')

@unauthenticated_user
def accountCreatedSuccess(request):
    context={'val':True}
    return render(request, 'accounts/accountCreated.html', context) 

@unauthenticated_user
def deptregisterPage(request):
    form = DepartmentSignUpForm()
    if request.method == 'POST':
        form = DepartmentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, user)
            # user_v = UserVendor.get()
            return redirect('accountCreatedSuccess')
            # return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/registerDepartment.html', context)

@unauthenticated_user
def vendregisterPage(request):
    form = VendorSignUpForm()
    if request.method == 'POST':
        form = VendorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, user)
            
            return redirect('accountCreatedSuccess')
            # return redirect('login')
            

    context = {'form':form}
    return render(request, 'accounts/registerVendor.html', context)

@unauthenticated_user
def registerPage(request):
    return render(request, 'accounts/register.html')

# @unauthenticated_user
# def loginPage(request):
#     return render(request, 'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

        
    else:
        if request.method == 'POST':
            email = request.POST.get('username')
            password = request.POST.get('password')
            print("Email: " + email)
            print("Password: " + password)
            
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                print("Goign Home!")
                return redirect('home')

        context = {}
        return render(request, 'accounts/login.html', context)


# @unauthenticated_user
# class DepartmentSignUpView(CreateView):
#     model = Account
#     form_class = DepartmentSignUpForm
#     template_name = 'registerDepartment.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'user_dept'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         return redirect('login')
#         # login(self.request, user)


# # @unauthenticated_user
# class DepartmentSignUpView(CreateView):
#     model = Account
#     form_class = VendorSignUpForm
#     template_name = 'registerVendor.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'user_vendor'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         return redirect('login')
#         # login(self.request, user)

