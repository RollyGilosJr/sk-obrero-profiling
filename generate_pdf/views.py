
from django.db.models.functions import Lower
from django.http import  HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.utils.text import slugify

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



from io import StringIO, BytesIO

from profiling.models import Profile


@login_required
def generate_document(response):
    current_user = response.user
    #
    # if response.method == "POST":
    #     datas = response.POST.get("header_input")
    #     datas_code = slugify(datas)
    #
    #
    #     datas = {"header": datas, "code":datas_code}
    # else:
    #     datas = ""
    # global val
    # def val():
    #     return datas
    # profiles = Profile.objects.all()

    education_years = []
    # for profile in profiles:
    #     years = profile.education_year
    #
    #     if years not in education_years and profile.education_level != "College" and profile.education_level != "Graduates" and profile.education_level != "Out of School":
    #         education_years.append(years)
    # if Profile.objects.filter(education_level="College"):
    #     education_years.append("College")
    # if Profile.objects.filter(education_level="Graduates") :
    #     education_years.append("Graduates")
    # if Profile.objects.filter(education_level="Out of School"):
    #     education_years.append("Out of School")
    # print(education_years)
    templist = []
    # for years in education_years:
    #     if years == "Out of School":
    #         year_code = years.replace(" ","")
    #     else:
    #         year_code = years.replace("Grade ","")
    #     # print(year_code)
    #     # print(year_code)
    #     templist.append({"grade":years, "code":year_code})

    # print(templist)


    return render(response,'dashboard/generate_document.html',{
        'current_user': current_user,
        # 'datas':datas,
        # 'templist':templist,

    })

def pdf(response):
    record = Profile.objects.all().order_by("last_name")
    return render(response,'pdf/pdf.html',{
        "record":record
    })

@login_required
def getPdfPage(request):
    # ok = val()
    # print("OK", ok)
    # print(type(ok))
    # header = ok["header"]
    # print(header)

    #
    # if grade == "College":
    #     records = Profile.objects.filter(education_level="College").order_by(Lower("last_name"))
    # elif grade == "OutofSchool":
    #     records = Profile.objects.filter(education_level="Out of School").order_by(Lower("last_name"))
    # elif grade == "Graduates":
    #     records = Profile.objects.filter(education_level="Graduates").order_by(Lower("last_name"))
    # else:
    #     records = Profile.objects.filter(education_year="Grade " + grade).order_by(Lower("last_name"))
    #
    # data = {'record': records, "grade": grade, "header": header,}
    record = Profile.objects.all().order_by("last_name")
    print(record)
    data = {"record":record}

    template = get_template("pdf/pdf.html")
    data_p = template.render(data)
    response = BytesIO()

    pdfPage = pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")), response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(), content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")