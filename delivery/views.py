from django.shortcuts import render,redirect,reverse
from .forms import AddDeliveryModeForm,onTransitForm
from order.models import OrderNumberPartner,OrderItemPartner
from django.http import HttpResponseRedirect
from .models import Ontransit,DeliveredOrder
from accounting.models import OrderInvoice
from accounting.forms import OrderDebitForm
from django.contrib import messages
from accounting.models import OrderDebit


# Create your views here.
# add deliverymode
def addDeliveryModeView(request):
    form = AddDeliveryModeForm
    if request.method == "POST":
        form=AddDeliveryModeForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request,'addDeliveryMode.html',{"form":form})
# edit deliverymode
# delete delivery

# dispatch
def createDispatchView(request,id):
    form = onTransitForm
    orders=OrderNumberPartner.objects.get(pk=id)
    orderitems = OrderItemPartner.objects.filter(orderNumber=orders)
    orderinvoice=OrderInvoice.objects.filter(order=orders)
    form = onTransitForm(initial={"orderNumber":orders})
    if request.method=="POST":
        form = onTransitForm(request.POST)
        if form.is_valid():
            captain=form.cleaned_data['captain']
            form.save()

 
            return redirect("orderList_url")

    return render(request,'createDispatch.html',{"orders":orders,"orderitems":orderitems,"form":form})

def makeDeliveryView(request):
    currentUser = request.user
    orderNumberFilter= request.GET.get('order_number')
    transitOrder=Ontransit.objects.filter(captain=currentUser)
    if orderNumberFilter is not None:
        order = OrderNumberPartner.objects.get(order_number=orderNumberFilter)
        url = reverse('initiateDelivery_url', args=[order.order_number])
        return redirect(url)

    return render(request,'makeDelivery.html',{"transitOrder":transitOrder})


def initiateDeliveryView(request,orderNumber):
    orderNumberFilter= request.GET.get('order_number')
    order = OrderNumberPartner.objects.get(order_number=orderNumber)
    orderNumber=Ontransit.objects.filter(orderNumber=order)
    orderItems = OrderItemPartner.objects.filter(orderNumber=order)
    print('orderNumber',orderNumberFilter)

    if orderNumberFilter is not None:
        order = OrderNumberPartner.objects.get(order_number=orderNumberFilter)
        url = reverse('deliveryPaymentView_url', args=[order.order_number])
        return redirect(url)

 
    
    return render (request,'initateDelivery.html',{"orderNumber":orderNumber,"orderItems":orderItems})

def deliveryPaymentView(request,orderNumber):
    order = OrderNumberPartner.objects.get(order_number=orderNumber)
    orderitems = OrderItemPartner.objects.filter(orderNumber=order)
    form = OrderDebitForm
    ontransit=Ontransit.objects.get(orderNumber = order)
    pre_total = []
    orderInvoice=OrderInvoice.objects.get(order=order)
    

    for i in orderitems:
        i.quantity*i.product.product_price
        pre_total.append(i.quantity*i.product.product_price)

    expected_payment=sum(pre_total)

    if request.method == 'POST':
        form = OrderDebitForm(request.POST)
        if form.is_valid():
            unsavedform=form.save(commit=False)
            paid_amount=form.cleaned_data["amount"]
      
            if paid_amount < expected_payment:
                messages.error(request,'Amount is lower than expected amount')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                
                unsavedform.order  =  ontransit.orderNumber 
                unsavedform.invoice = orderInvoice
                unsavedform.partner = order.partner
                DeliveredOrder.objects.create( orderNumber = ontransit.orderNumber,deliveryMode=ontransit.deliveryMode,captain=ontransit.captain)
                Ontransit.objects.filter(pk=ontransit.pk).delete()
                messages.success(request,'Payment Succesfull')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                



        
    return render(request,'deliveryPayment.html',{
                            "order":order,
                            'expected_payment':expected_payment,
                            'form':form,
                            
                            })