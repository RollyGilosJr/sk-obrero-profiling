import os

from appdirs import unicode
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from reportlab.lib.units import inch
from django.contrib.auth.decorators import login_required

import sk_profiling.settings
from sk_profiling import settings
from .models import Profile
from django.utils.text import slugify
from .forms import profile_form
# TODO: Try using forms and add class to it
# Create your views here.


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


@login_required
def dashboard(response):
    current_user = response.user

    total_profile = Profile.objects.all().count
    elem_level = Profile.objects.filter(educational_background = "Elementary Level").count()
    elem_grad = Profile.objects.filter(educational_background = "Elementary Graduate").count()
    hs_level = Profile.objects.filter(educational_background = "High School Level").count()
    hs_grad = Profile.objects.filter(educational_background = "High School Graduate").count()
    voc_grad = Profile.objects.filter(educational_background = "Vocational Graduate").count()
    col_level = Profile.objects.filter(educational_background = "College Level").count()
    col_grad = Profile.objects.filter(educational_background = "College Graduate").count()
    master_level = Profile.objects.filter(educational_background = "Masters Level").count()
    master_grad = Profile.objects.filter(educational_background = "Masters Graduate").count()
    doct_level = Profile.objects.filter(educational_background = "Doctorate Level").count()
    doct_grad = Profile.objects.filter(educational_background = "Doctorate Graduate").count()

    sex_data = {
        "Male":Profile.objects.filter(sex="Male").count(),
        "Female":Profile.objects.filter(sex="Female").count()
    }

    civil_status_data = {
        "Single":Profile.objects.filter(civil_status="Single").count(),
        "Married":Profile.objects.filter(civil_status="Married").count(),
        "Widowed":Profile.objects.filter(civil_status="Widowed").count(),
        "Divorced":Profile.objects.filter(civil_status="Divorced").count(),
        "Separated":Profile.objects.filter(civil_status="Separated").count(),
        "Annulled":Profile.objects.filter(civil_status="Annulled").count(),
        "Unknown":Profile.objects.filter(civil_status="Unknown").count(),
        "Live-in":Profile.objects.filter(civil_status="Live").count(),
    }
    youth_classification_data = {
        "In School Youth":Profile.objects.filter(youth_classification="In School Youth").count(),
        "Out of School youth":Profile.objects.filter(youth_classification="Out of School youth").count(),
        "Working Youth":Profile.objects.filter(youth_classification="Working Youth").count(),
        "Person with Disability":Profile.objects.filter(youth_classification="Person with Disability").count(),
        "Children in Conflict with Law":Profile.objects.filter(youth_classification="Children in Conflict with Law").count(),
        "Indigenous People":Profile.objects.filter(youth_classification="Indigenous People").count(),
    }
    youth_age_group_date = {
        "Child Youth":Profile.objects.filter(youth_age_group="Child Youth").count(),
        "Core Youth":Profile.objects.filter(youth_age_group="Core Youth").count(),
        "Young Adult":Profile.objects.filter(youth_age_group="Young Adult").count(),
    }

    work_status_data = {
        "Employed":Profile.objects.filter(work_status="Employed").count(),
        "Unemployed":Profile.objects.filter(work_status="Unemployed").count(),
        "Self-Employed":Profile.objects.filter(work_status="Self-Employed").count(),
        "Currently Looking For a Job":Profile.objects.filter(work_status="Currently Looking For a Job").count(),
        "Not interested Looking for a Job":Profile.objects.filter(work_status="Not interested Looking for a Job").count(),
    }
    
    educational_background_data = {
        "Elementary Level":Profile.objects.filter(educational_background="Self-Employed").count(),
        "Elementary Graduate":Profile.objects.filter(educational_background="Elementary Graduate").count(),
        "High School Level":Profile.objects.filter(educational_background="High School Level").count(),
        "High School Graduate":Profile.objects.filter(educational_background="High School Graduate").count(),
        "Vocational Graduate":Profile.objects.filter(educational_background="Vocational Graduate").count(),
        "College Level":Profile.objects.filter(educational_background="College Level").count(),
        "College Graduate":Profile.objects.filter(educational_background="College Graduate").count(),
        "Masters Level":Profile.objects.filter(educational_background="Masters Level").count(),
        "Masters Graduate":Profile.objects.filter(educational_background="Masters Graduate").count(),
        "Doctorate Level":Profile.objects.filter(educational_background="Doctorate Level").count(),
        "Doctorate Graduate":Profile.objects.filter(educational_background="Doctorate Graduate").count(),
    }

    sk_voter_data ={
        "Yes":Profile.objects.filter(sk_voter="Yes").count(),
        "No":Profile.objects.filter(sk_voter="No").count(),
    }
    national_voter_data ={
        "Yes":Profile.objects.filter(national_voter="Yes").count(),
        "No":Profile.objects.filter(national_voter="No").count(),
    }
    print(sk_voter_data)
    print(national_voter_data)
    



    return render(response, "dashboard/index.html",{
        "current_user":current_user,
        "total_profile":total_profile,
        
        "elem_level":elem_level,
        "elem_grad":elem_grad,
        "hs_level":hs_level,
        "hs_grad":hs_grad,
        "voc_grad":voc_grad,
        "col_level":col_level,
        "col_grad":col_grad,
        "master_level":master_level,
        "master_grad":master_grad,
        "doct_level":doct_level,
        "doct_grad":doct_grad,
        "sex_data":sex_data,
        "civil_status_data":civil_status_data,
        "youth_classification_data":youth_classification_data,
        "youth_age_group_date":youth_age_group_date,
        "work_status_data":work_status_data,
        "educational_background_data":educational_background_data,
        "sk_voter_data":sk_voter_data,
        "national_voter_data":national_voter_data,
    })
@login_required
def profile(response):
    datas = Profile.objects.all().order_by(Lower('last_name'))
    current_user = response.user

    return render(response, "profiles/profiles.html",{
        'datas':datas,
        'current_user': current_user,

    })

@login_required
def profile_page(response, slug):

    form = get_object_or_404(Profile, slug=slug)
    current_user = response.user

    if response.method == "POST":
        if response.POST.get("delete") != None:
            form.delete()
            return redirect('profiles')
        if response.POST.get("edit") != None:
            
            return redirect('profile_page_edit', slug)
    return render(response, "profiles/profile_page.html",{
        "form":form,
        'current_user': current_user,

    })


@login_required
def profile_page_edit(response,slug):
    obj = get_object_or_404(Profile, slug=slug)
    search = Profile.objects.get(slug=slug)
    form = profile_form(response.POST or None, instance=obj)
    
    # NOTE: Changes sa name ay kailangan tignan. Kapag nag edit ng name ang user tapos may kaparehas pala, mag tothrow ng error si system
    # So dapat unique padin pag inupdate ni user ang isang profile

    if form.is_valid():
        save = form.save(commit=False)
        # if may changes sa name - palitan din ang full_name tapos slug ng object
        if (search.first_name != save.first_name or search.middle_name != save.middle_name or search.last_name != save.last_name or search.suffix != save.suffix):
            
            if save.middle_name != None:
                if save.suffix != None:
                    save.full_name = save.last_name.title() + ", " + save.first_name.title() + " " + save.middle_name[0].title() + "., " + save.suffix.title()
                    save.slug = slugify(unicode(save.full_name))
                    print(save.slug)
                    if Profile.objects.filter(first_name = save.first_name.title(), middle_name=save.middle_name.title(), last_name=save.last_name.title(), suffix=save.suffix.title()).exists():
                        messages.error(response, messages.error, "")
                        return HttpResponseRedirect(profile_page,save.slug)
                else:
                    save.full_name = save.last_name.title() + ", " + save.first_name.title() + " " + save.middle_name[0].title() + "."
                    save.slug = slugify(unicode(save.full_name))
                    print(save.slug)
                    if Profile.objects.filter(first_name = save.first_name.title(), middle_name=save.middle_name.title(), last_name=save.last_name.title()).exists():
                        messages.error(response, messages.error, "")
                        return HttpResponseRedirect(profile_page,save.slug)
            else:
                if save.suffix != None:
                    save.full_name = save.last_name.title() + ", " + save.first_name.title() + ", "+ save.suffix.title()
                    save.slug = slugify(unicode(save.full_name))
                    print(save.slug)
                    if Profile.objects.filter(first_name = save.first_name.title(), last_name=save.last_name.title(), suffix=save.suffix.title()).exists():
                        messages.error(response, messages.error, "")
                        return HttpResponseRedirect(profile_page,save.slug)
                else:
                    save.full_name = save.last_name.title() + ", " + save.first_name.title()
                    save.slug = slugify(unicode(save.full_name))
                    print(save.slug)
                    if Profile.objects.filter(first_name = save.first_name.title(), last_name=save.last_name.title()).exists():
                        messages.error(response, messages.error, "")
                        return HttpResponseRedirect(profile_page,save.slug)
                
        # if walang changes sa name save na agad
        save.save()

        return redirect(profile_page,save.slug)
    current_user = response.user
    return render(response, "profiles/profile_page_edit.html", {
        "obj":obj,
        "form":form,
        "current_user":current_user


    })
@login_required
def add_profile(response):
    form = profile_form()
    current_user = response.user

    if response.method == "POST":
        print("POST")
        form = profile_form(response.POST)
        
        if form.is_valid():
            save = form.save(commit=False)

            if save.middle_name != None:
                if save.suffix != None:
                    save.full_name = save.last_name.title() + ", " + save.first_name.title() + " " + save.middle_name[0].title() + "., " + save.suffix.title()
                    save.slug = slugify(unicode(save.full_name))
                    print(save.slug)
                    if Profile.objects.filter(first_name = save.first_name.title(), middle_name=save.middle_name.title(), last_name=save.last_name.title(), suffix=save.suffix.title()).exists():
                        messages.error(response, messages.error, "")
                        return HttpResponseRedirect(response.path)
                else:
                    save.full_name = save.last_name.title() + ", " + save.first_name.title() + " " + save.middle_name[0].title() + "."
                    save.slug = slugify(unicode(save.full_name))
                    print(save.slug)
                    if Profile.objects.filter(first_name = save.first_name.title(), middle_name=save.middle_name.title(), last_name=save.last_name.title()).exists():
                        messages.error(response, messages.error, "")
                        return HttpResponseRedirect(response.path)
            else:
                if save.suffix != None:
                    save.full_name = save.last_name.title() + ", " + save.first_name.title() + ", "+ save.suffix.title()
                    save.slug = slugify(unicode(save.full_name))
                    print(save.slug)
                    if Profile.objects.filter(first_name = save.first_name.title(), last_name=save.last_name.title(), suffix=save.suffix.title()).exists():
                        messages.error(response, messages.error, "")
                        return HttpResponseRedirect(response.path)
                else:
                    save.full_name = save.last_name.title() + ", " + save.first_name.title()
                    save.slug = slugify(unicode(save.full_name))
                    print(save.slug)
                    if Profile.objects.filter(first_name = save.first_name.title(), last_name=save.last_name.title()).exists():
                        messages.error(response, messages.error, "")
                        return HttpResponseRedirect(response.path)
            save.save()

        return HttpResponseRedirect(response.path)

    return render(response,"profiles/add_profile.html",{
        "form":form,
        'current_user': current_user,

    })


# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa



# from io import StringIO, BytesIO


# val = None




# @login_required
# def generate_document(response):
#     current_user = response.user

#     if response.method == "POST":
#         datas = response.POST.get("header_input")
#         datas_code = slugify(datas)


#         datas = {"header": datas, "code":datas_code}
#     else:
#         datas = ""
#     global val
#     def val():
#         return datas
#     profiles = Profile.objects.all()

#     education_years = []
#     for profile in profiles:
#         years = profile.education_year

#         if years not in education_years and profile.education_level != "College" and profile.education_level != "Graduates" and profile.education_level != "Out of School":
#             education_years.append(years)
#     if Profile.objects.filter(education_level="College"):
#         education_years.append("College")
#     if Profile.objects.filter(education_level="Graduates") :
#         education_years.append("Graduates")
#     if Profile.objects.filter(education_level="Out of School"):
#         education_years.append("Out of School")
#     print(education_years)
#     templist = []
#     for years in education_years:
#         if years == "Out of School":
#             year_code = years.replace(" ","")
#         else:
#             year_code = years.replace("Grade ","")
#         # print(year_code)
#         # print(year_code)
#         templist.append({"grade":years, "code":year_code})

#     print(templist)


#     return render(response,'dashboard/generate_document.html',{
#         'current_user': current_user,
#         'datas':datas,
#         'templist':templist,

#     })

# def pdf(response):
#     return render(response,'pdf.html',{
#     })

# @login_required
# def getPdfPage(request, grade, header):
#     ok = val()
#     print("OK", ok)
#     print(type(ok))
#     header = ok["header"]
#     print(header)


#     if grade == "College":
#         records = Profile.objects.filter(education_level="College").order_by(Lower("last_name"))
#     elif grade == "OutofSchool":
#         records = Profile.objects.filter(education_level="Out of School").order_by(Lower("last_name"))
#     elif grade == "Graduates":
#         records = Profile.objects.filter(education_level="Graduates").order_by(Lower("last_name"))
#     else:
#         records = Profile.objects.filter(education_year="Grade " + grade).order_by(Lower("last_name"))

#     data = {'record': records, "grade": grade, "header": header,}


#     template = get_template("pdf.html")
#     data_p = template.render(data)
#     response = BytesIO()

#     pdfPage = pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")), response)
#     if not pdfPage.err:
#         return HttpResponse(response.getvalue(), content_type="application/pdf")
#     else:
#         return HttpResponse("Error Generating PDF")

