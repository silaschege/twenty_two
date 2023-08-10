from django.shortcuts import render,redirect,reverse
from .models import (   
                    SupplierInvoice,
                    SupplierDebit,
                    SupplierBulkDebit,
                    SupplierPaymentBalance,
                    OrderInvoice
                    )
from .forms import (
                    SupplierSearchForm,
                    SupplierBulkDebitForm,
                    PartnerSearchForm,
                    )
from supplier.models import SupplierDetailModel
from django.contrib import messages
# Create your views here.
def AllSupplierAccountsView(request):
    searchSupplier = SupplierSearchForm
    supplier=SupplierInvoice.objects.all()
    supplier_id= request.GET.get('supplier_number')

    # SEARCH FOR SUPPLIER IN INVOICES
    results = []
    if 'supplierSearchQuery' in request.GET:
        searchSupplier = SupplierSearchForm(request.GET)
        
        if searchSupplier.is_valid():
            query = searchSupplier.cleaned_data['supplierSearchQuery']
            results= SupplierInvoice.objects.filter(supplier__supplier_name__icontains = query)
    

    # id instance
    if supplier_id is not None:

        url = reverse('supplierAcountDetail_url', args=[supplier_id])
        return redirect(url)
    return render(request,'allSupplierAccounts.html',{
                                                    "results":results,
                                                    "supplier":supplier,
                                                    "searchSupplier":searchSupplier
                                                    })

def supplierAcountDetailView(request,id):
    supplierInvoices=SupplierInvoice.objects.filter(supplier=id)
    return render(request,'supplierAccountDetail.html',{
                                                        "supplierInvoices":supplierInvoices,
                                                        })

def supplierAcountDetailView(request,id):
    supplierId= request.GET.get('supplier_id')
    supplierInvoices=SupplierInvoice.objects.filter(supplier=id)
    supplierDebit = SupplierDebit.objects.filter(supplier=id)
    specificsupplier= SupplierDetailModel.objects.get(pk=id)
    
    # id instance
    if supplierId is not None:
        url = reverse('supplierAccountDebit_url', args=[supplierId])
        return redirect(url)
    
    return render(request,'supplierAccountDetail.html',{
                                                        "supplierInvoices":supplierInvoices,
                                                        "supplierDebit":supplierDebit,
                                                        "specificsupplier":specificsupplier
                                                        })

def supplierAccountDebitView(request, id):
    initialsupplier = SupplierDetailModel.objects.get(pk=id)
    currentUser = request.user
    form = SupplierBulkDebitForm(initial={"supplier": initialsupplier})

    if request.method == "POST":
        form = SupplierBulkDebitForm(request.POST)

        if form.is_valid():
            bulkamount = form.cleaned_data['bulkamount']
            unsaved = form.save(commit=False)
            unsaved.paidby = currentUser

            # Step 3: Debit invoices according to bulk amount
            if bulkamount > 0:
                unsaved.save()

                # Get supplier invoices and the latest bulk debit payment
                supplier = SupplierInvoice.objects.filter(supplier=initialsupplier)
                bulkfilter = SupplierBulkDebit.objects.filter(supplier=initialsupplier, paidby=currentUser).latest('id')
                bulkamountbalance = bulkamount
                outstandingbalane = SupplierPaymentBalance.objects.filter(supplier=initialsupplier)
                outstandingbalanecount = outstandingbalane.count()

                if outstandingbalanecount > 0:
                    # Pay outstanding supplier payments
                    for outstanding in outstandingbalane:
                        paibleamount = SupplierInvoice.objects.get(receivedcategory=outstanding.receivedcategory)
                        balance = paibleamount.amount - outstanding.paid_amount
                        bulkamountbalance = bulkamountbalance - balance
                        messages.success(request, 'Payment is done 0')

                        if bulkamountbalance >= 0:
                            # Pay the whole balance
                            SupplierDebit.objects.create(
                                supplier=outstanding.supplier,
                                receivedcategory=outstanding.receivedcategory,
                                paidby=currentUser,
                                bulkpayment=outstanding.bulkpayment,
                                amount=outstanding.paid_amount,
                            )
                            SupplierDebit.objects.create(
                                supplier=outstanding.supplier,
                                receivedcategory=outstanding.receivedcategory,
                                paidby=currentUser,
                                bulkpayment=bulkfilter,
                                amount=balance,
                            )
                            outstanding.delete()
                            messages.success(request, 'Payment is done 1')
                        else:
                            # Pay a portion of the outstanding balance
                            SupplierPaymentBalance.objects.create(
                                supplier=outstanding.supplier,
                                receivedcategory=outstanding.receivedcategory,
                                paidby=currentUser,
                                bulkpayment=bulkfilter,
                                paid_amount=bulkamount,
                            )
                            messages.success(request, 'Payment is done 2')

                # Pay supplier invoices if bulk amount is left
                for i in supplier:
                    if bulkamountbalance > 0:
                        transactionbBalance = bulkamountbalance - i.amount

                        if transactionbBalance >= 0:
                            # Pay the whole invoice amount
                            SupplierDebit.objects.create(
                                supplier=i.supplier,
                                receivedcategory=i.receivedcategory,
                                paidby=currentUser,
                                bulkpayment=bulkfilter,
                                amount=i.amount,
                            )
                            bulkamountbalance -= i.amount
                            messages.success(request, 'Payment is done')

                        else:
                            # Pay a portion of the invoice amount
                            SupplierPaymentBalance.objects.create(
                                supplier=i.supplier,
                                receivedcategory=i.receivedcategory,
                                paidby=currentUser,
                                bulkpayment=bulkfilter,
                                paid_amount=bulkamountbalance,
                            )
                            bulkamountbalance = 0
                            messages.success(request, 'Payment is done')

            else:
                messages.error(request, 'Payment is zero')

    return render(request, 'makeSupplierDebit.html', {"form": form})

def allPartnerAccountsView(request):
    form = PartnerSearchForm
    partnerID = request.GET.get('partner_id')
    # SEARCH FOR PARTNER IN INVOICES
    results = []
    if 'partnerSearchQuery' in request.GET:
        form = PartnerSearchForm(request.GET)
        
        if form.is_valid():
            query = form.cleaned_data['partnerSearchQuery']
            results= OrderInvoice.objects.filter(order__partner__businessName__icontains = query)

    orderInvoice=OrderInvoice.objects.filter().distinct()
    # id instance
    if partnerID is not None:

        url = reverse('partnerAccountStatement_url', args=[partnerID])
        return redirect(url)
   
    return render(request,'allPartnerAccounts.html',{
                                                    "results":results,
                                                    "form":form,
                                                    "orderInvoice":orderInvoice
                                                    })


def partnerAccountStatementView(request,id):
    orderInvoice=OrderInvoice.objects.filter(order__partner=id)
    return render(request,'partnerAccountStatement.html',{
                            "orderInvoice":orderInvoice
                            })

# def supplierAccountDebitView(request,id):
#     initialsupplier=SupplierDetailModel.objects.get(pk=id)
#     currentUser=request.user
#     form=SupplierBulkDebitForm(initial={"supplier":initialsupplier})
#     if request.method=="POST":
#         form=SupplierBulkDebitForm(request.POST)
#         if form.is_valid():
#             bulkammount=form.cleaned_data['bulkamount']
#             unsaved=form.save(commit=False)
#             unsaved.paidby = currentUser
            

#             # debit invoices according to bulk amount
#                 # check if bulk amount is more than 0
#                 # check for balances first 
#                 # if balances are present pay balances
#                 # check for other outstanding transactions 
#                 # check everytime if amount can pay outstanding transaction
#                 # pay outstanding transaction 
#                 # if not possible pay for a portion of the outstanding balance which is another model

           
            
#                  # check if bulk amount is more than 0
#             if  bulkammount>0:
#                      # check for balances first 
#                     unsaved.save()
#                     supplier=SupplierInvoice.objects.filter(supplier = initialsupplier)
#                     bulkfilter=SupplierBulkDebit.objects.filter(supplier=initialsupplier, paidby=currentUser).latest('id')
#                     bulkamountbalance = 0 
#                     outstandingbalane=SupplierPaymentBalance.objects.filter(supplier = initialsupplier)
#                     outstandingbalanecount= outstandingbalane.count()
                    
#                     if outstandingbalanecount >0:
#                         for outstanding in outstandingbalane:
#                             paibleamount=SupplierInvoice.objects.get(receivedcategory=outstanding.receivedcategory)
#                             balance=paibleamount.amount-outstanding.paid_amount
#                             bulkamountbalance=bulkammount-balance
#                             # check if bulk amount can pay the whole balance
#                             if bulkamountbalance >0:
                             
#                                 # update the table with prevoius bulk payments and then also add the current bulk payment
#                                 SupplierDebit.objects.create(
#                                 supplier  = outstanding.supplier,
#                                 receivedcategory = outstanding.receivedcategory,
#                                 paidby =currentUser ,
#                                 bulkpayment =outstanding.bulkpayment ,
#                                 amount=outstanding.paid_amount,
#                                 )
#                                 SupplierDebit.objects.create(
#                                 supplier  = outstanding.supplier,
#                                 receivedcategory = outstanding.receivedcategory,
#                                 paidby =currentUser ,
#                                 bulkpayment =bulkfilter ,
#                                 amount=balance,
#                                 )
#                                 outstanding.delete()
#                                 messages.success(request,'Payment is done 1')
#                             if bulkamountbalance<0:
#                                 SupplierPaymentBalance.objects.create(
#                                         supplier  = outstanding.supplier,
#                                         receivedcategory = outstanding.receivedcategory,
#                                         paidby = currentUser,
#                                         bulkpayment = bulkfilter,
#                                         paid_amount = bulkammount,
#                                         )
#                                 messages.success(request,'Payment is done 2')

#                 # check for other outstanding transactions 
#                 # check everytime if amount can pay outstanding transaction
#                 # pay outstanding transaction 
#                 # if not possible pay for a portion of the outstanding balance which is another model

#                     for i in supplier:
#                         if bulkamountbalance > 0:
#                             transactionbBalance=bulkamountbalance-i.amount
#                             if transactionbBalance >0:
#                                 SupplierDebit.objects.create(
#                                 supplier  = i.supplier,
#                                 receivedcategory = i.receivedcategory,
#                                 paidby =currentUser ,
#                                 bulkpayment = bulkfilter ,
#                                 amount=i.amount,
#                             )
#                                 messages.success(request,'Payment is done')
#                             if transactionbBalance < 0:
#                                 SupplierPaymentBalance.objects.create(
#                             supplier  = outstanding.supplier,
#                             receivedcategory = outstanding.receivedcategory,
#                             paidby = currentUser,
#                             bulkpayment = bulkfilter,
#                             paid_amount = bulkamountbalance,
#                                         )
#             else:
#                 messages.error(request,'Payment is zero')

#     return render(request,'makeSupplierDebit.html',{"form":form})
