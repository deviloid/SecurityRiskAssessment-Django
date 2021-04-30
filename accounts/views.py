from django.http.response import HttpResponse
from riskassessment.models import *
from django.db import reset_queries
from django.shortcuts import render, redirect, HttpResponseRedirect

# from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import Account
from department.models import Department, UserDepartment
from vendor.models import UserVendor, Vendor
from product.models import Product
from .forms import *
from riskassessment.forms import (
    AvailabiltyCriticalityForm,
    CloudServiceForm,
    ComplianceForm,
    DatabaseServersForm,
    DeptInfoForm,
    EncryptionForm,
    IntegrationForm,
    QAEnvironmentForm,
    SecMatEvidenceForm,
    SWIntegrityForm,
    SecureCommsForm,
    SecureDesignForm,
    VendInfoForm,
    DataManagementForm,
)

# from .forms import DepartmentSignUpForm, VendorSignUpForm

# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    if request.user == None:
        return redirect("login")
    if request.user.is_uservendor:
        user_v = UserVendor.objects.get(user_id=request.user.id).userType_id
        if user_v != 3:
            return redirect("vendorRoleError")
    # context = {'user':request.user}
    # user_v = UserVendor.objects.get(user_id=request.user.id)
    # e = UserVendor(user=request.user, userType_id=3)
    # e.eval_score (e_score/e.max_score)*100
    # e.save()
    # print(user_v)
    # print(request.user.id)
    return render(request, "dashboard/dashboard.html")


@unauthenticated_user
def accountCreatedSuccess(request):
    context = {"val": True}
    return render(request, "accounts/accountCreated.html", context)


@login_required(login_url="login")
def deptregisterPage(request):
    userform = SignUpForm()
    user_info = DeptCreateForm()
    user_type = "Department"
    if request.method == "POST":
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
            return redirect("usersView")

    context = {"userform": userform, "user_info": user_info, "user_type": user_type}
    return render(request, "dashboard/create-new-user.html", context)


@login_required(login_url="login")
def vendregisterPage(request):
    userform = SignUpForm()
    user_info = VendCreateForm()
    user_type = "Vendor"
    if request.method == "POST":
        userform = SignUpForm(request.POST)
        user_info = VendCreateForm(request.POST)
        if userform.is_valid() and user_info.is_valid():
            user = userform.save(commit=False)
            user.is_uservendor = True
            password = Account.objects.make_random_password()
            user.set_password(password)
            userform.save()
            vend_user = user_info.save(commit=False)
            vend_user.user_id = user.id
            user_info.save()
            return redirect("usersView")

    context = {"userform": userform, "user_info": user_info, "user_type": user_type}
    return render(request, "dashboard/create-new-user.html", context)


@login_required(login_url="login")
def home(request):
    return render(request, "accounts/index.html")
    # return render(request, "dashboard/dashboard.html")


@unauthenticated_user
def registerPage(request):
    return render(request, "accounts/register.html")


# @unauthenticated_user
# def loginPage(request):
#     return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect("login")


@unauthenticated_user
def loginPage(request):

    if request.user.is_authenticated:
        return redirect("home")

    else:
        if request.method == "POST":
            email = request.POST.get("username")
            password = request.POST.get("password")
            print("Email: " + email)
            print("Password: " + password)

            user = authenticate(request, email=email, password=password)

            if user is not None:
                if user.has_setpsd == False:
                    Account.objects.filter(id=user.id).update(has_setpsd=True)

                login(request, user)
                print("Goign Home!")
                return redirect("home")

        context = {}
        return render(request, "accounts/login.html", context)


@login_required(login_url="login")
def UsersView(request):
    ras = Account.objects.filter(is_staff=True)
    dept_users = UserDepartment.objects.all().order_by("department")
    vend_users = UserVendor.objects.all()

    context = {"ras": ras, "dept_users": dept_users, "vend_users": vend_users}
    return render(request, "dashboard/dashboard-users.html", context)


@login_required(login_url="login")
def ProductsView(request):
    products = Product.objects.all().order_by("name")

    context = {"products": products}
    return render(request, "dashboard/dashboard-products.html", context)


@login_required(login_url="login")
def AddProduct(request):
    form = ProductCreateForm()
    if request.method == "POST":
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ProductsView")

    context = {
        "form": form,
    }
    return render(request, "dashboard/create-new-product.html", context)


@login_required(login_url="login")
def ViewProduct(request, pk, slug):

    product = Product.objects.get(id=pk, slug=slug)
    departments = RiskAssessment.objects.filter(product_id=product.id).values_list('department__name','department__location').distinct()

    context = {"product": product, "departments": departments}
    return render(request, "dashboard/view_product.html", context)


@login_required(login_url="login")
def DepartmentView(request):

    departments = Department.objects.all().order_by("name")

    context = {"departments": departments}
    return render(request, "dashboard/dashboard-department.html", context)


@login_required(login_url="login")
def ViewDepartment(request, slug):

    department = Department.objects.get(slug=slug)
    users = UserDepartment.objects.filter(department_id=department.id)

    products = RiskAssessment.objects.filter(department_id=department.id).values_list('product__name','product__vendor__name', 'product__slug', 'product_id').distinct()

    context = {"users": users, "department": department, "products":products}
    return render(request, "dashboard/view_department.html", context)


def VendorView(request):

    vendors = Vendor.objects.all().order_by("name")

    context = {"vendors": vendors}
    return render(request, "dashboard/dashboard-vendor.html", context)


@login_required(login_url="login")
def ViewVendor(request, slug):

    vendor = Vendor.objects.get(slug=slug)
    products = Product.objects.filter(vendor_id=vendor.id)
    user = UserVendor.objects.filter(vendor_id=vendor.id)
    if len(user) != 0:
        user = user[0]
    else:
        user = None

    context = {"user": user, "products": products, "vendor": vendor}
    return render(request, "dashboard/view_vendor.html", context)


@login_required(login_url="login")
def AddDepartment(request):
    form = DepartmentCreateForm()
    if request.method == "POST":
        form = DepartmentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("DepartmentView")

    context = {
        "form": form,
    }
    return render(request, "dashboard/create-new-department.html", context)


@login_required(login_url="login")
def AddVendor(request):
    form = VendorCreateForm()
    if request.method == "POST":
        form = VendorCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("VendorView")

    context = {
        "form": form,
    }
    return render(request, "dashboard/create-new-vendor.html", context)


def RiskAssessmentsView(request):

    riskassessments = RiskAssessment.objects.filter(approved=False)

    context = {"riskassessments": riskassessments}

    return render(request, "dashboard/dashboard-risk_assessment.html", context)

def ClosedRiskAssessmentsView(request):

    riskassessments = RiskAssessment.objects.filter(approved=True)

    context = {"riskassessments": riskassessments}

    return render(request, "dashboard/dashboard-risk_assessment_closed.html", context)

def AddRiskAssessment(request):

    form = CreateRAForm()
    if request.method == "POST":
        form = CreateRAForm(request.POST)
        if form.is_valid():
            ra = form.save(commit=False)
            ra.ra = request.user
            form.save()
            pk = ra.product.id
            pk2 = ra.id
            slug = ra.product.slug
            print(pk)
            return redirect("step1", p_id=pk, ra_id=pk2, slug=slug)

    context = {"form": form}

    return render(request, "dashboard/create-risk_assessment.html", context)


def test2(request):
    form1 = DeptInfoForm()
    form2 = VendInfoForm()
    form3 = DataManagementForm()
    form4 = AvailabiltyCriticalityForm()
    form5 = ComplianceForm()
    form6 = SecMatEvidence()
    form7 = IntegrationForm()
    form8 = CloudServiceForm()
    form9 = SecureDesignForm()
    form10 = EncryptionForm()
    form11 = QAEnvironmentForm()
    form12 = DatabaseServersForm()
    form13 = SecureCommsForm()
    form14 = SWIntegrityForm()

    context = {
        "form1": form1,
        "form2": form2,
        "form3": form3,
        "form4": form4,
        "form5": form5,
        "form6": form6,
        "form7": form7,
        "form8": form8,
        "form9": form9,
        "form10": form10,
        "form11": form11,
        "form12": form12,
        "form13": form13,
        "form14": form14,
    }

    return render(request, "accounts/test.html", context=context)


def RA_step1(request, p_id, slug, ra_id):

    progress = 0
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    DeptInfoForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )
    DeptInfoForm.base_fields["mpc"] = forms.ModelChoiceField(
        queryset=UserDepartment.objects.filter(department_id=riskassessment.department.id),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Main Project Contact",
        label="Main Project Contact",
    )

    inst = DeptInfo.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = DeptInfoForm(request.POST or None, initial=initial)
    else:
        form = DeptInfoForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = DeptInfoForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 1
                riskassessment.save()
            return redirect("step2", slug=slug1, p_id=p_id1, ra_id=ra_id1)

    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/start-ra.html", context)


def RA_step2(request, p_id, slug, ra_id):

    progress = round(100 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    exst_contract = Vendor.objects.get(id=riskassessment.product.vendor.id).exstContract
    mpc_name =  str(UserVendor.objects.get(vendor_id=riskassessment.product.vendor.id).user.fname + " "+UserVendor.objects.get(vendor_id=riskassessment.product.vendor.id).user.lname)
    mpc_email = UserVendor.objects.get(vendor_id=riskassessment.product.vendor.id).user.email
    mpc_phone = UserVendor.objects.get(vendor_id=riskassessment.product.vendor.id).phone
    print(type(mpc_name))
    initial = {
        "riskassessment": riskassessment,
        "exst_contract":exst_contract,
        "mpc_name":mpc_name,
        "mpc_email":mpc_email,
        "mpc_phone":mpc_phone
    }

    VendInfoForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )
    
    inst = VendInfo.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = VendInfoForm(request.POST or None, initial=initial)
    else:
        form = VendInfoForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = VendInfoForm(request.POST, instance=inst)
        if form.is_valid():
            ra = form.save(commit=False)
            if inst == None:
                ra.mpc_name = str(UserVendor.objects.get(vendor_id=riskassessment.product.vendor.id).user.fname + " "+UserVendor.objects.get(vendor_id=riskassessment.product.vendor.id).user.lname)
                ra.mpc_email = UserVendor.objects.get(vendor_id=riskassessment.product.vendor.id).user.email
                ra.mpc_phone = UserVendor.objects.get(vendor_id=riskassessment.product.vendor.id).phone
                riskassessment.steps_complete = 2
                riskassessment.save()
            ra.save()

            return redirect("step3", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step2.html", context)


def RA_step3(request, p_id, slug, ra_id):

    progress = round(200 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    DataManagementForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = DataManagement.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = DataManagementForm(request.POST or None, initial=initial)
    else:
        form = DataManagementForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = DataManagementForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 3
                riskassessment.save()
            return redirect("step4", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step3.html", context)


def RA_step4(request, p_id, slug, ra_id):

    progress = round(300 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    AvailabiltyCriticalityForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = AvailabiltyCriticality.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = AvailabiltyCriticalityForm(request.POST or None, initial=initial)
    else:
        form = AvailabiltyCriticalityForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = AvailabiltyCriticalityForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 4
                riskassessment.save()
            return redirect("step5", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step4.html", context)


def RA_step5(request, p_id, slug, ra_id):

    progress = round(400 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    ComplianceForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = Compliance.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = ComplianceForm(request.POST or None, initial=initial)
    else:
        form = ComplianceForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = ComplianceForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 5
                riskassessment.save()
            return redirect("step6", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step5.html", context)


def RA_step6(request, p_id, slug, ra_id):

    progress = round(500 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    SecMatEvidenceForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = SecMatEvidence.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = SecMatEvidenceForm(request.POST or None, initial=initial)
    else:
        form = SecMatEvidenceForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = SecMatEvidenceForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 6
                riskassessment.save()
            return redirect("step7", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step6.html", context)


def RA_step7(request, p_id, slug, ra_id):

    progress = round(600 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    IntegrationForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = Integration.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = IntegrationForm(request.POST or None, initial=initial)
    else:
        form = IntegrationForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = IntegrationForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 7
                riskassessment.save()
            return redirect("step8", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step7.html", context)


def RA_step8(request, p_id, slug, ra_id):

    progress = round(700 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    CloudServiceForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = CloudService.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = CloudServiceForm(request.POST or None, initial=initial)
    else:
        form = CloudServiceForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = CloudServiceForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 8
                riskassessment.save()
            return redirect("step9", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step8.html", context)


def RA_step9(request, p_id, slug, ra_id):

    progress = round(800 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    SecureDesignForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = SecureDesign.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = SecureDesignForm(request.POST or None, initial=initial)
    else:
        form = SecureDesignForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = SecureDesignForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 9
                riskassessment.save()
            return redirect("step10", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step9.html", context)


def RA_step10(request, p_id, slug, ra_id):

    progress = round(900 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    EncryptionForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = Encryption.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = EncryptionForm(request.POST or None, initial=initial)
    else:
        form = EncryptionForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = EncryptionForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 10
                riskassessment.save()
            return redirect("step11", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step10.html", context)


def RA_step11(request, p_id, slug, ra_id):

    progress = round(1000 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    QAEnvironmentForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = QAEnvironment.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = QAEnvironmentForm(request.POST or None, initial=initial)
    else:
        form = QAEnvironmentForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = QAEnvironmentForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 11
                riskassessment.save()
            return redirect("step12", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step11.html", context)


def RA_step12(request, p_id, slug, ra_id):

    progress = round(1100 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    DatabaseServersForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )
    inst = DatabaseServers.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = DatabaseServersForm(request.POST or None, initial=initial)
    else:
        form = DatabaseServersForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = DatabaseServersForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 12
                riskassessment.save()

            return redirect("step13", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step12.html", context)


def RA_step13(request, p_id, slug, ra_id):

    progress = round(1200 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    SecureCommsForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = SecureComms.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = SecureCommsForm(request.POST or None, initial=initial)
    else:
        form = SecureCommsForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = SecureCommsForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            if inst == None:
                riskassessment.steps_complete = 13
                riskassessment.save()
            return redirect("step14", slug=slug1, p_id=p_id1, ra_id=ra_id1)
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step13.html", context)


def RA_step14(request, p_id, slug, ra_id):

    progress = round(1300 / 14, 2)
    p_id1 = p_id
    slug1 = slug
    ra_id1 = ra_id
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    initial = {
        "riskassessment": riskassessment,
    }

    SWIntegrityForm.base_fields["riskassessment"] = forms.ModelChoiceField(
        queryset=RiskAssessment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Assessment",
    )

    inst = SWIntegrity.objects.filter(riskassessment_id=ra_id)
    if inst.count() == 0:
        inst = None
    else:
        inst = inst[0]

    if inst == None:
        form = SWIntegrityForm(request.POST or None, initial=initial)
    else:
        form = SWIntegrityForm(instance=inst, initial=initial)

    if request.method == "POST":
        if inst:
            form = SWIntegrityForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            riskassessment.evaluated = False
            riskassessment.save()
            if inst == None:
                riskassessment.steps_complete = 14
                riskassessment.save()
            return redirect("RiskAssessmentsView")
    context = {
        "form": form,
        "riskassessment": riskassessment,
        "progress": progress,
        "inst": inst,
    }
    return render(request, "riskassessment/ra-step14.html", context)


def RiskAssessmentDetail(request, p_id, slug, ra_id):

    ra = RiskAssessment.objects.get(id=ra_id)
    prod = Product.objects.get(id=ra.product_id)
    dept_info = DeptInfo.objects.get(riskassessment_id=ra_id)
    vend_info = VendInfo.objects.get(riskassessment_id=ra_id)

    data_mng_score = -1
    a_c_score = -1
    comp_score = -1
    sec_mat_score = -1
    inte_score = -1
    csm_score = -1
    sd_score = -1
    enc_score = -1
    qa_score = -1
    dbserver_score = -1
    sec_comm_score = -1
    sw_inte_score = -1

    data_mng = DataManagement.objects.filter(riskassessment_id=ra_id)
    if data_mng.count() == 0:
        data_mng = "Not Filled"
    else:
        data_mng_score = data_mng[0].eval_score
        data_mng = "Filled"
    a_c = AvailabiltyCriticality.objects.filter(riskassessment_id=ra_id)
    if a_c.count() == 0:
        a_c = "Not Filled"
    else:
        a_c_score = a_c[0].eval_score
        a_c = "Filled"
    comp = Compliance.objects.filter(riskassessment_id=ra_id)
    if comp.count() == 0:
        comp = "Not Filled"
    else:
        comp_score = comp[0].eval_score
        comp = "Filled"
    sec_mat = SecMatEvidence.objects.filter(riskassessment_id=ra_id)
    if sec_mat.count() == 0:
        sec_mat = "Not Filled"
    else:
        sec_mat_score = sec_mat[0].eval_score
        sec_mat = "Filled"
    inte = Integration.objects.filter(riskassessment_id=ra_id)
    if inte.count() == 0:
        inte = "Not Filled"
    else:
        inte_score = inte[0].eval_score
        inte = "Filled"
    csm = CloudService.objects.filter(riskassessment_id=ra_id)
    if csm.count() == 0:
        csm = "Not Filled"
    else:
        csm_score = csm[0].eval_score
        csm = "Filled"
    sd = SecureDesign.objects.filter(riskassessment_id=ra_id)
    if sd.count() == 0:
        sd = "Not Filled"
    else:
        sd_score = sd[0].eval_score
        sd = "Filled"
    enc = Encryption.objects.filter(riskassessment_id=ra_id)
    if enc.count() == 0:
        enc = "Not Filled"
    else:
        enc_score = enc[0].eval_score
        enc = "Filled"
    qa = QAEnvironment.objects.filter(riskassessment_id=ra_id)
    if qa.count() == 0:
        qa = "Not Filled"
    else:
        qa_score = qa[0].eval_score
        qa = "Filled"
    dbserver = DatabaseServers.objects.filter(riskassessment_id=ra_id)
    if dbserver.count() == 0:
        dbserver = "Not Filled"
    else:
        dbserver_score = dbserver[0].eval_score
        dbserver = "Filled"
    sec_comm = SecureComms.objects.filter(riskassessment_id=ra_id)
    if sec_comm.count() == 0:
        sec_comm = "Not Filled"
    else:
        sec_comm_score = sec_comm[0].eval_score
        sec_comm = "Filled"
    sw_inte = SWIntegrity.objects.filter(riskassessment_id=ra_id)
    if sw_inte.count() == 0:
        sw_inte = "Not Filled"
    else:
        sw_inte_score = sw_inte[0].eval_score
        sw_inte = "Filled"

    context = {
        "ra": ra,
        "prod": prod,
        "dept_info": dept_info,
        "vend_info": vend_info,
        "data_mng": data_mng,
        "data_mng_score": data_mng_score,
        "a_c": a_c,
        "a_c_score": a_c_score,
        "comp": comp,
        "comp_score": comp_score,
        "sec_mat": sec_mat,
        "sec_mat_score": sec_mat_score,
        "inte": inte,
        "inte_score": inte_score,
        "csm": csm,
        "csm_score": csm_score,
        "sd": sd,
        "sd_score": sd_score,
        "enc": enc,
        "enc_score": enc_score,
        "qa": qa,
        "qa_score": qa_score,
        "dbserver": dbserver,
        "dbserver_score": dbserver_score,
        "sec_comm": sec_comm,
        "sec_comm_score": sec_comm_score,
        "sw_inte": sw_inte,
        "sw_inte_score": sw_inte_score,
    }

    return render(request, "dashboard/view_risk-assessment.html", context)


def score_evaluate(request, ra_id):
    data_mng = DataManagement.objects.get(riskassessment_id=ra_id)
    data_mng_score = 0
    if data_mng.recs_purged == "Yes":
        data_mng_score += 3
    if data_mng.data_process_outside == "Yes":
        data_mng_score += 3
    if data_mng.data_stored_outside == "YES":
        data_mng_score += 3
    if data_mng.data_rcvd_outside == "Yes":
        data_mng_score += 3
    if data_mng.data_accss_outside == "Yes":
        data_mng_score += 3

    a_c = AvailabiltyCriticality.objects.get(riskassessment_id=ra_id)
    a_c_score = 0
    if a_c.a_rating == "Tier 1":
        a_c_score += 5
    if a_c.a_rating == "Tier 2":
        a_c_score += 3
    if a_c.a_rating == "Tier 3":
        a_c_score += 1
    if a_c.c_rating == "High":
        a_c_score += 5
    if a_c.c_rating == "Medium":
        a_c_score += 3
    if a_c.c_rating == "Low":
        a_c_score += 1

    comp = Compliance.objects.get(riskassessment_id=ra_id)
    comp_score = 0
    if comp.sso == "No":
        comp_score += 3
    if comp.audit_req_std_comp == "No":
        comp_score += 3
    if comp.auto_patch == "No":
        comp_score += 3

    sec_mat = SecMatEvidence.objects.get(riskassessment_id=ra_id)
    sec_mat_score = 0
    if sec_mat.attst_o_comp == "No":
        sec_mat_score += 3
    if sec_mat.soc2_reports == "No":
        sec_mat_score += 3
    if sec_mat.ann_pen_scan_results == "No":
        sec_mat_score += 3
    if sec_mat.ann_wa_vuln_scan == "No":
        sec_mat_score += 3

    inte = Integration.objects.get(riskassessment_id=ra_id)
    inte_score = 0
    if inte.sso == "No":
        inte_score += 3
    if inte.mfa == "No":
        inte_score += 3
    if inte.adfs == "No":
        inte_score += 3

    csm = CloudService.objects.get(riskassessment_id=ra_id)
    csm_score = 0
    if csm.saas_sol == "No":
        csm_score += 1
    if csm.iaas_hosted == "No":
        csm_score += 1
    if csm.on_prem == "No":
        csm_score += 1

    sd = SecureDesign.objects.get(riskassessment_id=ra_id)
    sd_score = 0
    if sd.q1 == "No":
        sd_score += 5
    if sd.q2 == "No":
        sd_score += 5
    if sd.q3 == "No":
        sd_score += 3
    if sd.q4 == "No":
        sd_score += 3
    if sd.q5 == "No":
        sd_score += 2
    if sd.q6 == "No":
        sd_score += 1
    enc = Encryption.objects.get(riskassessment_id=ra_id)
    enc_score = 0
    if enc.p1q1 == "No":
        enc_score += 5
    if enc.p1q2 == "No":
        enc_score += 5
    if enc.p1q3 == "No":
        enc_score += 5
    if enc.p1q4 == "No":
        enc_score += 1
    if enc.p1q5 == "No":
        enc_score += 1
    if enc.p1q6 == "No":
        enc_score += 1
    if enc.p1q7 == "No":
        enc_score += 1
    if enc.p1q8 == "No":
        enc_score += 1
    if enc.p1q9 == "No":
        enc_score += 1
    if enc.p2q1 == "No":
        enc_score += 5
    if enc.p2q2 == "No":
        enc_score += 5
    if enc.p2q3 == "No":
        enc_score += 3
    if enc.p2q4 == "No":
        enc_score += 3
    if enc.p2q5 == "No":
        enc_score += 2
    if enc.p2q6 == "No":
        enc_score += 1
    if enc.p2q7 == "No":
        enc_score += 1
    qa = QAEnvironment.objects.get(riskassessment_id=ra_id)
    qa_score = 0
    if qa.q1 == "No":
        qa_score += 5
    if qa.q2 == "No":
        qa_score += 3
    if qa.q3 == "No":
        qa_score += 2
    if qa.q4 == "No":
        qa_score += 1
    if qa.q5 == "No":
        qa_score += 1
    dbserver = DatabaseServers.objects.get(riskassessment_id=ra_id)
    dbserver_score = 0
    if dbserver.q1 == "No":
        dbserver_score += 5
    if dbserver.q2 == "No":
        dbserver_score += 3
    if dbserver.q3 == "No":
        dbserver_score += 2
    if dbserver.q4 == "No":
        dbserver_score += 1
    if dbserver.q5 == "No":
        dbserver_score += 1
    if dbserver.q6 == "No":
        dbserver_score += 1
    sec_comm = SecureComms.objects.get(riskassessment_id=ra_id)
    sec_comm_score = 0
    if sec_comm.q1 == "No":
        sec_comm_score += 5
    if sec_comm.q2 == "No":
        sec_comm_score += 5
    if sec_comm.q3 == "No":
        sec_comm_score += 3
    if sec_comm.q4 == "No":
        sec_comm_score += 2
    if sec_comm.q5 == "No":
        sec_comm_score += 2
    if sec_comm.q6 == "No":
        sec_comm_score += 1
    if sec_comm.q7 == "No":
        sec_comm_score += 1
    if sec_comm.q8 == "No":
        sec_comm_score += 1
    sw_inte = SWIntegrity.objects.get(riskassessment_id=ra_id)
    sw_inte_score = 0
    if sw_inte.q1 == "No":
        sw_inte_score += 5
    if sw_inte.q2 == "No":
        sw_inte_score += 5
    if sw_inte.q3 == "No":
        sw_inte_score += 3
    if sw_inte.q4 == "No":
        sw_inte_score += 2
    if sw_inte.q5 == "No":
        sw_inte_score += 2

    data_mng.score = data_mng_score
    data_mng.eval_score = (data_mng_score / data_mng.max_score) * 100
    data_mng.save()
    a_c.score = a_c_score
    a_c.eval_score = (a_c_score / a_c.max_score) * 100
    a_c.save()
    comp.score = comp_score
    comp.eval_score = (comp_score / comp.max_score) * 100
    comp.save()
    sec_mat.score = sec_mat_score
    sec_mat.eval_score = (sec_mat_score / sec_mat.max_score) * 100
    sec_mat.save()
    inte.score = inte_score
    inte.eval_score = (inte_score / inte.max_score) * 100
    inte.save()
    csm.score = csm_score
    csm.eval_score = (csm_score / csm.max_score) * 100
    csm.save()
    sd.score = sd_score
    sd.eval_score = (sd_score / sd.max_score) * 100
    sd.save()
    enc.score = enc_score
    enc.eval_score = (enc_score / enc.max_score) * 100
    enc.save()
    qa.score = qa_score
    qa.eval_score = (qa_score / qa.max_score) * 100
    qa.save()
    dbserver.score = dbserver_score
    dbserver.eval_score = (dbserver_score / dbserver.max_score) * 100
    dbserver.save()
    sec_comm.score = sec_comm_score
    sec_comm.eval_score = (sec_comm_score / sec_comm.max_score) * 100
    sec_comm.save()
    sw_inte.score = sw_inte_score
    sw_inte.eval_score = (sw_inte_score / sw_inte.max_score) * 100
    sw_inte.save()

    ra = RiskAssessment.objects.get(id=ra_id)
    ra.evaluated = True
    ra.save()

    product = ra.product

    return redirect(
        "RiskAssessmentDetail", slug=product.slug, p_id=product.id, ra_id=ra_id
    )

def ApproveRA(request, ra_id, slug, p_id):

    if request.user.is_staff and not request.user.is_superuser:
        ra = RiskAssessment.objects.get(id=ra_id)
        ra.approved = True
        ra.save()
        return redirect("ClosedRiskAssessmentsView")
    
    return redirect("RiskAssessmentsView")



def test4(request):

    ra = RiskAssessment.objects.get(id=5)
    steps_complete = 0
    a = [
        ra.ra_step1.all().count(),
        ra.ra_step2.all().count(),
        ra.ra_step3.all().count(),
        ra.ra_step4.all().count(),
        ra.ra_step5.all().count(),
        ra.ra_step6.all().count(),
        ra.ra_step7.all().count(),
        ra.ra_step8.all().count(),
        ra.ra_step9.all().count(),
        ra.ra_step10.all().count(),
        ra.ra_step11.all().count(),
        ra.ra_step12.all().count(),
        ra.ra_step13.all().count(),
        ra.ra_step14.all().count(),
    ]

    for b in a:
        steps_complete += b

    context = {"steps_complete": steps_complete}
    return render(request, "dashboard/test1.html", context)


# def ra_step_redirect(request, slug, p_id, ra_id, step):
#     if request.method=="GET":
#         if step == 2:
#             return redirect("step2", p_id=p_id, slug=slug, ra_id=ra_id)
#         if step == 3:
#             return redirect("step3", p_id=p_id, slug=slug, ra_id=ra_id)
#         if step == 4:
#             return redirect("step4", p_id=p_id, slug=slug, ra_id=ra_id)
#         if step == 5:
#             return redirect("step5", p_id=p_id, slug=slug, ra_id=ra_id)
#         if  step == 6:
#             return redirect("step6", p_id=p_id, slug=slug, ra_id=ra_id)
#         if step == 7:
#             return redirect("step7", p_id=p_id, slug=slug, ra_id=ra_id)
#         if step == 8:
#             return redirect("step8", p_id=p_id, slug=slug, ra_id=ra_id)
#         if step == 9:
#             return redirect("step9", p_id=p_id, slug=slug, ra_id=ra_id)
#         if step == 10:
#             return redirect("step10", p_id=p_id, slug=slug, ra_id=ra_id)
#         if step == 11:
#             return redirect("step11", p_id=p_id, slug=slug, ra_id=ra_id)
#         if step == 12:
#             return redirect("step12", p_id=p_id, slug=slug, ra_id=ra_id)
#         if step == 13:
#             return redirect("step13", p_id=p_id, slug=slug, ra_id=ra_id)
#         else:
#             return redirect("RiskAssessmentsView")


# def step2(request):
#     form = VendInfoForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             pet = form.save(commit=False)
#             person = Person.objects.create(fn=request.session["step1"])
#             pet.owner = person
#             pet.save()
#             return HttpResponseRedirect("finished")
#     context = {"form": form}
#     return render(request, "accounts/test.html", context)


# @unauthenticated_user
# class DepartmentSignUpView(CreateView):
#     model = Account
#     form_class = DepartmentSignUpForm
#     template_name = 'registerDepartment.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'user_dept'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
# form.eval_score = (fform_score/form.max_score)*100        user =
# form.save()
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
# form.eval_score = (fform_score/form.max_score)*100        user =
# form.save()
#         return redirect('login')
#         # login(self.request, user)
