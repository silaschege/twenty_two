from django.shortcuts import render,redirect
from .models import (
                    ProductModel,
                    ProductCategoryModel,
                    ReceiveGoodsCategoryModelHolder,
                    ReceiveGoodsDetailHolderModel,
                    ReceiveGoodsCategoryModel,
                    ReceiveGoodsDetailModel
                    )
from .forms import (    
                    AddProductModelForm,
                    AddProductCategoryForm,
                    SearchSupplierForm,SearchProductForm,
                    AddReceiveGoodsDetailForm,
                    ProductPricingForm,

                    )
from django.contrib import messages
from django.http import HttpResponseRedirect
from supplier.models import SupplierDetailModel
from accounting.models import SupplierInvoice

# Create your views here.

# add product category
def addProductCategoryView(request):
    form=AddProductCategoryForm
    if request.method == 'POST':
        form = AddProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Category added succesfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    category=ProductCategoryModel.objects.all().order_by('-id')

    return render(request,'addProductCategory.html',{"form":form,"category":category})

# add product 
def addProductView(request):
    form=AddProductModelForm
    if request.method == 'POST':
        form = AddProductModelForm(request.POST)
        if form.is_valid():
            product=form.save(commit=False)
            product.product_quantity=0
            product.product_price = 0
            product.save()
            messages.success(request,'Product added succesfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    return render(request,'addProduct.html',{"form":form})


# allproducts
def allProductView(request):
    product = ProductModel.objects.all()
    
    return render(request,'allProducttemplate.html',{'product':product})

def receiveMerchandizeSupplierView(request):
    form = SearchSupplierForm
    supplier_id = request.GET.get('supplier_id')
   
    currentUser= request.user

    # search supplier
    supplierResult = []
    if 'searchSupplier' in request.GET:
        form = SearchSupplierForm(request.GET)
        if form.is_valid():
            searchSupplier=form.cleaned_data['searchSupplier']
            supplierResult=SupplierDetailModel.objects.filter(supplier_name__icontains=searchSupplier)
    if supplier_id is not None:
        selectedSupplier = SupplierDetailModel.objects.get(pk=supplier_id)
        ReceiveGoodsCategoryModelHolder.objects.create(supplier=selectedSupplier,receivedBY=currentUser)
    try:
        receivedSupplier=ReceiveGoodsCategoryModelHolder.objects.filter(receivedBY=currentUser).latest('id')
    except ReceiveGoodsCategoryModelHolder.DoesNotExist:
        receivedSupplier = None
    return render(request,"receiveMerchandizeSupplier.html",{
                                                            "form":form,
                                                            "supplierResult":supplierResult,
                                                            "receivedSupplier":receivedSupplier
                                                            })

def receiveMerchandizeProductView(request):
    currentUser= request.user
    product_id=request.GET.get('product_id')

    form=SearchProductForm
    productForm=AddReceiveGoodsDetailForm
    # search product
    productResult = []
    if 'searchProduct' in request.GET:
        form = SearchProductForm(request.GET)
        if form.is_valid():
            searchProduct=form.cleaned_data['searchProduct']
            productResult=ProductModel.objects.filter(product_name__icontains=searchProduct)
    receivedSupplier=ReceiveGoodsCategoryModelHolder.objects.filter(receivedBY=currentUser).latest('id')


    # initial values
    if product_id is not None:
        product = ProductModel.objects.get(pk=product_id)
        productForm=AddReceiveGoodsDetailForm(initial={"product":product})
    else:
        productForm=AddReceiveGoodsDetailForm()

    # product form insert
    if request.method=="POST":
       productForm=AddReceiveGoodsDetailForm(request.POST)
       if productForm.is_valid():
           productsave=productForm.save(commit=False)
           productsave.receive_goods_category=receivedSupplier
           product=productForm.cleaned_data['product']
        #    check if product has already been added
           receivedItemCheck=ReceiveGoodsDetailHolderModel.objects.filter(receive_goods_category=receivedSupplier,product=product)
           if receivedItemCheck.exists():
               
               ReceiveGoodsDetailHolderModel.objects.filter(receive_goods_category=receivedSupplier,product=product).delete()
               productsave.save()
               messages.error(request,'Receive Product Override')
               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
           else:
            productsave.save()
            messages.success(request,'Product received')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    receivedItems=ReceiveGoodsDetailHolderModel.objects.filter(receive_goods_category=receivedSupplier)

    # order totals 
    pretotal=[]
    for i in receivedItems:
       itemTotal= i.buying_price*i.quantity
       pretotal.append(itemTotal)
    
    orderTotal=sum(pretotal)

    return render(request,'receiveMerchandizeProduct.html',{
                                                            "form":form,
                                                            "receivedSupplier":receivedSupplier,
                                                            "productResult":productResult,
                                                            "productForm":productForm,
                                                            "receivedItems":receivedItems,
                                                            "orderTotal":orderTotal
                                                            })

# finalize receiving products
def finalizeReceiveProductsView(request):
    currentUser= request.user
    totalforOrder=[]
    receivedSupplier=ReceiveGoodsCategoryModelHolder.objects.filter(receivedBY=currentUser).latest('id')
    supplier = SupplierDetailModel.objects.get(pk=receivedSupplier.supplier.id)
    receivedItems=ReceiveGoodsDetailHolderModel.objects.filter(receive_goods_category=receivedSupplier)
    # order total 
    for i in receivedItems:
        itemtotal=i.buying_price*i.quantity
        totalforOrder.append(itemtotal)
    ordertotal=sum(totalforOrder)
    ReceiveGoodsCategoryModel.objects.create(supplier=supplier,receivedBY=currentUser,total=ordertotal)
    receivedCategory=ReceiveGoodsCategoryModel.objects.filter(receivedBY=currentUser).latest('id')
    
    
    #  received items
    pretotal=[]
    for i in receivedItems:
       productGet=ProductModel.objects.get(pk=i.product.id)
       ReceiveGoodsDetailModel.objects.create(
                                                receive_goods_category=receivedCategory,
                                                product=productGet,
                                                buying_price =i.buying_price,
                                                quantity=i.quantity,
                                                selling_price=0
                                                )
       itemtotal=i.buying_price*i.quantity
       pretotal.append(itemtotal)
       ReceiveGoodsDetailHolderModel.objects.filter(pk=i.id).delete()

    totalOrder=sum(pretotal)
    
    # invoice supplier
    SupplierInvoice.objects.create( supplier= supplier,receivedcategory=receivedCategory,receivedby = currentUser,amount=totalOrder)
    ReceiveGoodsCategoryModelHolder.objects.filter(receivedBY=currentUser).latest('id').delete()

    messages.success(request,'Items received succesfully')

    


    return redirect('productPricing_url')

def productPricingView(request):
    product_id=request.GET.get('product_id')
    received_id=request.GET.get('received_id')
    form= ProductPricingForm
    receivedItems = ReceiveGoodsDetailModel.objects.filter(selling_price=0)

    if received_id is not None:
        receivedItemInitial= ReceiveGoodsDetailModel.objects.get(pk=received_id)
        product=ProductModel.objects.get(pk=product_id)
        form = ProductPricingForm(initial={"product":product,
                                            "buying_price":receivedItemInitial.buying_price,
                                            "quantity":receivedItemInitial.quantity,
                                            })
        

    if request.method=="POST":
        form=ProductPricingForm(request.POST)
        if form.is_valid():
            sellingPrice=form.cleaned_data['selling_price']
            ReceiveGoodsDetailModel.objects.filter(pk=received_id).update(selling_price=sellingPrice)
            received= ReceiveGoodsDetailModel.objects.get(pk=received_id)
            product=ProductModel.objects.get(pk=product_id)
            newquantity=product.product_quantity+received.quantity
            ProductModel.objects.filter(pk=product_id).update(product_price=sellingPrice,product_quantity=newquantity)
            messages.success(request,'Price Updated')
            return HttpResponseRedirect(request.meta.get('HTTP_REFERER'))

    return render(request,'productPricing.html',{"receivedItems":receivedItems,"form":form})



# # add products
# def addProductsView(request):


#             return redirect("AllProducts")
#     return render(request,'addProduct.html',{"form":form})