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
    path('dashboard/users/register-dept-user/', views.deptregisterPage, name='register-dept-user'),
    path('dashboard/users/register-vend-user/', views.vendregisterPage, name='register-vend-user'),


    path('dashboard/products/', views.ProductsView, name="ProductsView"),
    path('dashboard/products/create-new-project/', views.AddProduct, name='AddProduct'),
    path('dashboard/products/<str:slug>/<str:pk>/view', views.ViewProduct, name='ViewProduct'),


    path('dashboard/department/', views.DepartmentView, name="DepartmentView"),
    path('dashboard/department/<str:slug>/view', views.ViewDepartment, name="ViewDepartment"),
    path('dashboard/department/add', views.AddDepartment, name="AddDepartment"),


    path('dashboard/vendor/', views.VendorView, name="VendorView"),
    path('dashboard/vendor/<str:slug>/view', views.ViewVendor, name="ViewVendor"),
    path('dashboard/vendor/add', views.AddVendor, name="AddVendor"),


    path('dashboard/risk-assessments/', views.RiskAssessmentsView, name="RiskAssessmentsView"),
    path('dashboard/risk-assessments-closed/', views.ClosedRiskAssessmentsView, name="ClosedRiskAssessmentsView"),
    path('dashboard/risk-assessments/add', views.AddRiskAssessment, name="AddRiskAssessment"),
    path('dashboard/risk-assessments/evaluate/<str:ra_id>', views.score_evaluate, name="EvaluateRiskAssessment"),
    

    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/approve', views.ApproveRA, name='ApproveRA'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/view', views.RiskAssessmentDetail, name='RiskAssessmentDetail'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/1/14', views.RA_step1, name='step1'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/2/14', views.RA_step2, name='step2'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/3/14', views.RA_step3, name='step3'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/4/14', views.RA_step4, name='step4'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/5/14', views.RA_step5, name='step5'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/6/14', views.RA_step6, name='step6'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/7/14', views.RA_step7, name='step7'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/8/14', views.RA_step8, name='step8'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/9/14', views.RA_step9, name='step9'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/10/14', views.RA_step10, name='step10'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/11/14', views.RA_step11, name='step11'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/12/14', views.RA_step12, name='step12'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/13/14', views.RA_step13, name='step13'),
    path('dashboard/risk-assessments/<str:slug>/<str:p_id>/<str:ra_id>/14/14', views.RA_step14, name='step14'),

    path('test/', views.test4, name="test4"),

    #PasswordReset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', form_class=UserPasswordResetForm),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html', form_class=UserPasswordChangeForm, success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('dashboard/risk-assessments/redirect/<str:slug>/<str:p_id>/<str:ra_id>/<str:step>/', views.ra_step_redirect, name='ra_step_redirect'),
    # url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
