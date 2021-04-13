"""sraToolDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm, UserPasswordChangeForm
# from department import views
# from vendor import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.registerPage, name="signup"),
    path('accountCreatedSuccess/', views.accountCreatedSuccess, name="accountCreatedSuccess"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/users/', views.UsersView, name="usersView"),
    path('dashboard/projects/', views.ProjectsView, name="ProjectsView"),
    path('dashboard/risk-assessments/', views.RiskAssessmentsView, name="RiskAssessmentsView"),
    # path('signup/department/', views.deptregisterPage, name='dept_signup'),
    path('dashboard/register-dept-user/', views.deptregisterPage, name='register-dept-user'),
    path('dashboard/register-vend-user/', views.vendregisterPage, name='register-vend-user'),
    path('dashboard/create-new-project/', views.AddProject, name='AddProject'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', form_class=UserPasswordResetForm),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html', form_class=UserPasswordChangeForm, success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('test/', views.test, name='test'),
    # url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
