from django.shortcuts import render
from .models import *

# Create your views here.
def GenReport(request, ra_id, p_id, slug):
    riskassessment = RiskAssessment.objects.get(id=ra_id)
    dept_info = DeptInfo.objects.get(riskassessment_id=ra_id)
    vend_info = VendInfo.objects.get(riskassessment_id=ra_id)
    data_mng = DataManagement.objects.get(riskassessment_id=ra_id)
    a_c = AvailabiltyCriticality.objects.get(riskassessment_id=ra_id)
    comp = Compliance.objects.get(riskassessment_id=ra_id)
    sec_mat = SecMatEvidence.objects.get(riskassessment_id=ra_id)
    inte = Integration.objects.get(riskassessment_id=ra_id)
    csm = CloudService.objects.get(riskassessment_id=ra_id)
    sd = SecureDesign.objects.get(riskassessment_id=ra_id)
    enc = Encryption.objects.get(riskassessment_id=ra_id)
    qa = QAEnvironment.objects.get(riskassessment_id=ra_id)
    dbserver = DatabaseServers.objects.get(riskassessment_id=ra_id)
    sec_comm = SecureComms.objects.get(riskassessment_id=ra_id)
    sw = SWIntegrity.objects.get(riskassessment_id=ra_id)

    reg_data = [reg_data.name for reg_data in data_mng.reg_data.all()]
    data_classi = [data_classi.name for data_classi in data_mng.data_classi.all()]

    context = {
        "riskassessment":riskassessment,
        "dept_info":dept_info,
        "vend_info":vend_info,
        "reg_data":reg_data,
        "data_classi":data_classi,
        "data_mng": data_mng,
        "a_c": a_c,
        "comp": comp,
        "sec_mat": sec_mat,
        "inte": inte,
        "csm": csm,
        "sd": sd,
        "enc": enc,
        "qa": qa,
        "dbserver": dbserver,
        "sec_comm": sec_comm,
        "sw": sw
    }

    return render(request, "riskassessment/generated-report.html", context)