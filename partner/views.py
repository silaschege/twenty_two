from django.shortcuts import render,redirect
from .forms import CreatePartnerBusinessForm,CreatePartnerAdminForm,CreateBusinessTypeForm
from .models import PartnerBusiness
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
# add partnerBusiness
def CreatePartnerView(request):
    form = CreatePartnerBusinessForm
    if request.method == "POST":
        form = CreatePartnerBusinessForm(request.POST)
        if form.is_valid():
            currentUser = request.user
            unsavedForm = form.save(commit=False)
            unsavedForm.registerBy = currentUser
            unsavedForm.save()
            return  redirect("CreatePartnerAdmin_url")
    return render(request,"CreatePartnerBusiness.html",{"form":form})
# add patneradmin
def CreatePartnerAdminView(request):
    form = CreatePartnerAdminForm
    currentUser = request.user
    partnerBusiness = PartnerBusiness.objects.filter(registerBy=currentUser).latest("id")
    if request.method == "POST":
        form = CreatePartnerAdminForm(request.POST)
        if form.is_valid():
            unsavedForm = form.save(commit=False)
            unsavedForm.business=partnerBusiness
            unsavedForm.save()
            messages.success(request,'Business partner created succesfully')
            return redirect("CreatePartner_url")
    
        
    return render(request,"CreatePartnerAdmin.html",{"form":form,"partnerBusiness":partnerBusiness})

def CreateBusinessTypeView(request):
    form=CreateBusinessTypeForm
    if request.method == "POST":
        form = CreateBusinessTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Business type created succesfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request,'createBusinessType.html',{"form":form})

# edit patnerdetails
# edit patneradmin
# delete patneradmin
# delete partner