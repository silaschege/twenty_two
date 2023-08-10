from django.shortcuts import render
from .forms import createSupplierForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def createSupplierView(request):
    form = createSupplierForm
    if request.method=="POST":
        form = createSupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Supplier created succesfully")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request,'createSupplier.html',{"form":form})
