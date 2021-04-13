from django.db import reset_queries
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import Account
from department.models import UserDepartment
from vendor.models import UserVendor
from project.models import Project
from.forms import SignUpForm, DeptCreateForm, VendCreateForm, ProjectCreateForm
from questionnaire.forms import VendInfoForm
# from .forms import DepartmentSignUpForm, VendorSignUpForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
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
    return render(request, 'dashboard/dashboard.html')

@unauthenticated_user
def accountCreatedSuccess(request):
    context={'val':True}
    return render(request, 'accounts/accountCreated.html', context) 

@login_required(login_url='login')
def deptregisterPage(request):
    userform = SignUpForm()
    user_info = DeptCreateForm()
    user_type = "Department"
    if request.method == 'POST':
        userform = SignUpForm(request.POST)
        user_info = DeptCreateForm(request.POST)
        if userform.is_valid() and user_info.is_valid():
            user = userform.save(commit=False)
            user.is_userdepartment = True
            password = Account.objects.make_random_password()
            user.set_password(password)
            userform.save()
            dept_user = user_info.save(commit=False)
            dept_user.user_id = user.id
            user_info.save()
            return redirect('usersView')

    context = {
        'userform':userform,
        'user_info':user_info,
        'user_type':user_type
        }
    return render(request, 'dashboard/create-new-user.html', context)

@login_required(login_url='login')
def vendregisterPage(request):
    userform = SignUpForm()
    user_info = VendCreateForm()
    user_type = "Vendor"
    if request.method == 'POST':
        userform = SignUpForm(request.POST)
        user_info = VendCreateForm(request.POST)
        if userform.is_valid() and user_info.is_valid():
            user = userform.save(commit=False)
            user.is_uservendor = True
            userform.save()
            vend_user = user_info.save(commit=False)
            vend_user.user_id = user.id
            user_info.save()

    context = {
        'userform':userform,
        'user_info':user_info,
        'user_type':user_type
        }
    return render(request, 'dashboard/create-new-user.html', context)

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/index.html')


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
    

@login_required(login_url='login')
def UsersView(request):
    ras = Account.objects.filter(is_staff=True)
    dept_users = UserDepartment.objects.all()
    vend_users = UserVendor.objects.all()

    context = {
        'ras':ras,
        'dept_users':dept_users,
        'vend_users':vend_users
        }
    return render(request, 'dashboard/dashboard-users.html', context)

    
@login_required(login_url='login')
def ProjectsView(request):
    projects = Project.objects.all()
    
    context = {
        'projects':projects        
        }
    return render(request, 'dashboard/dashboard-projects.html', context)


@login_required(login_url='login')
def AddProject(request):
    form = ProjectCreateForm()
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ProjectsView')
            
    context = {
        'form':form,
        }
    return render(request, 'dashboard/create-new-project.html', context)


def RiskAssessmentsView(request):

    return render(request, 'dashboard/risk-assessments.html')



def test(request):
    form = VendInfoForm()

    context = {
        'form':form
    }

    return render(request, 'accounts/test.html', context=context)
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

