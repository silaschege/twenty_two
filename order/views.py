from django.shortcuts import render,redirect,reverse
from accounting.models import OrderInvoice
from .form import ( 
                    SearchPartnerForm,
                    SearchProductForm,
                    OrderPartnerItemsHolderForm
                    )
from partner.models import PartnerBusiness
from .models import (
                    OrderNumberPartnerHolder,
                    OrderItemPartnerHolder,
                    OrderItemPartner,
                    OrderNumberPartner
                    )
from product.models import ProductModel
from django.http import HttpResponseRedirect
import uuid
from django.contrib import messages
# Create your views here.
# search for the partner
def createPartnerOrderView(request):
    searchPartner= SearchPartnerForm


    results = []
    if 'query' in request.GET:
        searchPartner= SearchPartnerForm(request.GET)
        
        if searchPartner.is_valid():
            query = searchPartner.cleaned_data['query']
            results= PartnerBusiness.objects.filter(businessName__icontains = query)
            
    return render(request,'createPartnerOrder.html',{"searchPartner":searchPartner,"results":results,})

# create the partner
def createPartner(request,id):
    partner = PartnerBusiness.objects.get(pk=id)
    currentUser = request.user
    # generate order number
    while True:
        orderNumber = str(uuid.uuid4()).replace('-', '').upper()
        # Check if order number already exists in the database
        if not OrderNumberPartner.objects.filter(order_number=orderNumber).exists():
            break
    OrderNumberPartnerHolder.objects.create(partner=partner,orderBy=currentUser,order_number=orderNumber)
    return redirect('createPartnerOrderItem_url')

# create the order items

def createPartnerOrderItemView(request):
    searchProduct = SearchProductForm
    orderItemForm = OrderPartnerItemsHolderForm
    currentUser = request.user
    product_id = request.GET.get('product_id')
    ordernumber=OrderNumberPartnerHolder.objects.filter(orderBy=currentUser).latest('id')
   
    
    # search for products
    results = []
    if 'productSearch' in request.GET:
        searchProduct = SearchProductForm(request.GET)
        
        if searchProduct.is_valid():
            query = searchProduct.cleaned_data['productSearch']
            results= ProductModel.objects.filter(product_name__icontains = query)
    
    # instance
    if product_id is not None:
        product = ProductModel.objects.get(pk=product_id)
        orderItemForm = OrderPartnerItemsHolderForm(initial={"product":product})
    else:
        orderItemForm = OrderPartnerItemsHolderForm()
    
    
    # form for order details
    if request.method == "POST":
        orderItemForm = OrderPartnerItemsHolderForm(request.POST)
        if orderItemForm.is_valid():
            orderNum=orderItemForm.save(commit=False)
            orderNum.orderNumber= ordernumber
            quantity=orderItemForm.cleaned_data['quantity'] 
            # check item availability
            if product.product_quantity < quantity:
                messages.error(request,'Quantity is over available')
            else:
                # check if item exists
                exist=OrderItemPartnerHolder.objects.filter(product=product_id)
                if exist.exists():
                    OrderItemPartnerHolder.objects.filter(product=product_id).delete()
                    messages.error(request,'Order overide')
                    orderNum.save()
                else:
                    messages.success(request,'order item added')
                    orderNum.save()
          
                    
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    Orderitems=OrderItemPartnerHolder.objects.filter(orderNumber=ordernumber.pk)
    pre_total=[]
    for i in Orderitems:
        pre_total.append(i.quantity * i.product.product_price)

    totalOrder=sum(pre_total)
    



    
    

    return render(request,'createPartnerOrderItems.html',{
                                                          "results":results,
                                                          "searchProduct":searchProduct,
                                                          "ordernumber":ordernumber,
                                                          "orderItemForm":orderItemForm,
                                                          "Orderitems":Orderitems,
                                                          "totalOrder":totalOrder,
                                                            })

# finalize the ordering process
def createOrderItemInstanceView(request):
    currentUser = request.user
    ordernumber=OrderNumberPartnerHolder.objects.filter(orderBy=currentUser).latest('id')
    ordernumberUUID=ordernumber.order_number
    orderitems=OrderItemPartnerHolder.objects.filter(orderNumber=ordernumber)
    pre_total=[]
    for i in orderitems:
        pre_total.append(i.quantity * i.product.product_price)

    totalOrder=sum(pre_total)
    OrderNumberPartner.objects.create(partner = ordernumber.partner,orderBy=ordernumber.orderBy,order_number=ordernumber.order_number,total=totalOrder)
    for i in orderitems:
        orderNUmberfilter=OrderNumberPartner.objects.get(order_number=i.orderNumber.order_number)
        OrderItemPartner.objects.create( orderNumber=orderNUmberfilter,product=i.product,quantity=i.quantity, )
        product=ProductModel.objects.get(id=i.product.id)
        newProductQuantity=product.product_quantity - i.quantity
        ProductModel.objects.filter(id=i.product.id).update(product_quantity=newProductQuantity)
        OrderItemPartnerHolder.objects.filter(pk=i.id).delete()
    OrderInvoice.objects.create(order=orderNUmberfilter,amount=totalOrder)
    OrderItemPartnerHolder.objects.filter(orderNumber=ordernumber).delete()

    
    
    return redirect('orderList_url')

def orderListView(request):
 
    order_number= request.GET.get('order_number')
    orders=OrderNumberPartner.objects.all().order_by('id')


     # instance
    if order_number is not None:
        order = OrderNumberPartner.objects.get(order_number=order_number)
        url = reverse('createDispatch_url', args=[order.id])
        return redirect(url)

     
    return render(request,'orderList.html',{"orders":orders,})




