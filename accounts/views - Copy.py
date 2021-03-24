from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from .decorators import unauthenticated_user
from .models import Account

# Create your views here.

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
#         login(self.request, user)
#         return redirect('home')




# @unauthenticated_user
# def registerPage(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, user)
#             return redirect('accountCreatedSuccess')
#             # return redirect('login')

#     context = {'form':form}
#     return render(request, 'accounts/register.html', context)

# @unauthenticated_user
# def accountCreatedSuccess(request):
#     return render(request, 'accounts/accountCreated.html')

# @unauthenticated_user
# def loginPage(request):

#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             print("Username: " + username)
#             print("Password: " + password)
            
#             user = authenticate(request, username=username, password=password)
            
#             if user is not None:
#                 login(request, user)
#                 print("Goign Home!")
#                 return redirect('home')

#         context = {}
#         return render(request, 'accounts/login.html', context)

# def logoutUser(request):
#     logout(request)
#     return redirect('login')

# @login_required(login_url='login')
# def home(request):
#     if request.user == None:
#         return redirect('login')
#     return render(request, 'accounts/dashboard.html')

# @login_required(login_url='login')
# def customer(request):
#     return render(request, 'accounts/customer.html')
#     # return HttpResponse('Customer')
