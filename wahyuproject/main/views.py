from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import FloatField, Sum, F
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .models import Products, Category, Subcategory, Distributors, User, Orders
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import View
from datetime import datetime
from django.utils.encoding import smart_str
from django.core.mail import send_mail
from django.conf import settings

import xlrd, csv

# Create your views here.
def index(request):
    category = Category.objects.all
    products = Products.objects.all
    content = {
        'title':"Wahyu Brand: No. 1 Sambal, Instant Pastes & Rempeyek Power!",
        'categories' : category,
        'products' : products
    }
    return render(request,'main/index.html', content)

def order(request):
    category = Category.objects.all
    products = Products.objects.all
    dist = Distributors.objects.all
    current_dist = Distributors.objects.filter(username__username=request.user.username)

    orders = Orders.objects.all

    if request.method == 'POST':
        
        neworder = Orders()
        neworder.orderno = "0"
        neworder.invoiceno = "/INV/VI/2015"
        neworder.name = request.POST.get("name")
        neworder.contactno = request.POST.get("contactno")
        neworder.email = request.POST.get("email")

        message = "Dear " + request.POST.get("name") + ", \nYour Order Details Below:\n\n"
        if request.user.is_authenticated:
            if request.user.is_staff:
                if request.POST.get("customerselect") != "Direct Sales":
                    neworder.distributor = Distributors.objects.get(username__username=request.POST.get('name'))
                else:
                    neworder.distributor = Distributors.objects.get(username__username="wahyu")
            else:
                neworder.distributor = Distributors.objects.get(username=request.user)
        else:
            neworder.distributor = Distributors.objects.get(username__username="wahyu")
        try:
            neworder.line1 = Products.objects.get(pk=int(request.POST.get("option1")))
            neworder.qty1 = request.POST.get('qty1')

            message = message + "1) " + neworder.line1.name + " : " + neworder.qty1 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line1.retailprice) + "\n"
            else:
                message = message + str(neworder.line1.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line1 = None
        try:
            neworder.line2 = Products.objects.get(pk=int(request.POST.get("option2")))
            neworder.qty2 = request.POST.get('qty2')
            message = message + "2) " + neworder.line2.name + " : " + neworder.qty2 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line2.retailprice) + "\n"
            else:
                message = message + str(neworder.line2.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line2 = None
        try:
            neworder.line3 = Products.objects.get(pk=int(request.POST.get('option3')))
            neworder.qty3 = request.POST.get('qty3')
            message = message + "3) " + neworder.line3.name + " : " + neworder.qty3 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line3.retailprice) + "\n"
            else:
                message = message + str(neworder.line3.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line3 = None
        try:
            neworder.line4 = Products.objects.get(pk=int(request.POST.get('option4')))
            neworder.qty4 = request.POST.get('qty4')
            message = message + "4) " + neworder.line4.name + " : " + neworder.qty4 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line4.retailprice) + "\n"
            else:
                message = message + str(neworder.line4.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line4 = None
        try:
            neworder.line5 = Products.objects.get(pk=int(request.POST.get('option5')))
            neworder.qty5 = request.POST.get('qty5')

            message = message + "5) " + neworder.line5.name + " : " + neworder.qty5 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line5.retailprice) + "\n"
            else:
                message = message + str(neworder.line5.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line5 = None
        try:
            neworder.line6 = Products.objects.get(pk=int(request.POST.get('option6')))
            neworder.qty6 = request.POST.get('qty6')

            message = message + "6) " + neworder.line6.name + " : " + neworder.qty6 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line6.retailprice) + "\n"
            else:
                message = message + str(neworder.line6.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line6 = None
        try:
            neworder.line7 = Products.objects.get(pk=int(request.POST.get('option7')))
            neworder.qty7 = request.POST.get('qty7')

            message = message + "7) " + neworder.line7.name + " : " + neworder.qty7 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line7.retailprice) + "\n"
            else:
                message = message + str(neworder.line7.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line7 = None
        try:
            neworder.line8 = Products.objects.get(pk=int(request.POST.get('option8')))
            neworder.qty8 = request.POST.get('qty8')

            message = message + "8) " + neworder.line8.name + " : " + neworder.qty8 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line8.retailprice) + "\n"
            else:
                message = message + str(neworder.line8.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line8 = None
        try:
            neworder.line9 = Products.objects.get(pk=int(request.POST.get('option9')))
            neworder.qty9 = request.POST.get('qty9')

            message = message + "9) " + neworder.line9.name + " : " + neworder.qty9 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line9.retailprice) + "\n"
            else:
                message = message + str(neworder.line9.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line9 = None
        try:
            neworder.line10 = Products.objects.get(pk=int(request.POST.get('option10')))
            neworder.qty10 = request.POST.get('qty10')

            message = message + "10) " + neworder.line10.name + " : " + neworder.qty10 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line10.retailprice) + "\n"
            else:
                message = message + str(neworder.line10.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line10 = None 
        try:      
            neworder.line11 = Products.objects.get(pk=int(request.POST.get('option11')))
            neworder.qty11 = request.POST.get('qty11')

            message = message + "11) " + neworder.line11.name + " : " + neworder.qty11 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line11.retailprice) + "\n"
            else:
                message = message + str(neworder.line11.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line11 = None
        try:
            neworder.line12 = Products.objects.get(pk=int(request.POST.get('option12')))
            neworder.qty12 = request.POST.get('qty12')

            message = message + "12) " + neworder.line12.name + " : " + neworder.qty12 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line12.retailprice) + "\n"
            else:
                message = message + str(neworder.line12.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line12 = None
        try:
            neworder.line13 = Products.objects.get(pk=int(request.POST.get('option13')))
            neworder.qty13 = request.POST.get('qty13')

            message = message + "13) " + neworder.line13.name + " : " + neworder.qty13 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line13.retailprice) + "\n"
            else:
                message = message + str(neworder.line13.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line13 = None
        try:
            neworder.line14 = Products.objects.get(pk=int(request.POST.get('option14')))
            neworder.qty14 = request.POST.get('qty14')

            message = message + "14) " + neworder.line14.name + " : " + neworder.qty14 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line14.retailprice) + "\n"
            else:
                message = message + str(neworder.line14.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line14 = None
        try:
            neworder.line15 = Products.objects.get(pk=int(request.POST.get('option15')))
            neworder.qty15 = request.POST.get('qty15')

            message = message + "15) " + neworder.line15.name + " : " + neworder.qty15 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line15.retailprice) + "\n"
            else:
                message = message + str(neworder.line15.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line15 = None
        try:
            neworder.line16 = Products.objects.get(pk=int(request.POST.get('option16')))
            neworder.qty16 = request.POST.get('qty16')

            message = message + "16) " + neworder.line16.name + " : " + neworder.qty16 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line16.retailprice) + "\n"
            else:
                message = message + str(neworder.line16.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line16 = None
        try:
            neworder.line17 = Products.objects.get(pk=int(request.POST.get('option17')))
            neworder.qty17 = request.POST.get('qty17')

            message = message + "17) " + neworder.line17.name + " : " + neworder.qty17 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line17.retailprice) + "\n"
            else:
                message = message + str(neworder.line17.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line17 = None
        try:
            neworder.line18 = Products.objects.get(pk=int(request.POST.get('option18')))
            neworder.qty18 = request.POST.get('qty18')

            message = message + "18) " + neworder.line18.name + " : " + neworder.qty18 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line18.retailprice) + "\n"
            else:
                message = message + str(neworder.line18.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line18 = None
        try:
            neworder.line19 = Products.objects.get(pk=int(request.POST.get('option19')))
            neworder.qty19 = request.POST.get('qty19')

            message = message + "19) " + neworder.line19.name + " : " + neworder.qty19 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line19.retailprice) + "\n"
            else:
                message = message + str(neworder.line19.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line19 = None
        try:
            neworder.line20 = Products.objects.get(pk=int(request.POST.get('option20')))
            neworder.qty20 = request.POST.get('qty20')

            message = message + "20) " + neworder.line20.name + " : " + neworder.qty20 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line20.retailprice) + "\n"
            else:
                message = message + str(neworder.line20.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line20 = None
        try:
            neworder.line21 = Products.objects.get(pk=int(request.POST.get('option21')))
            neworder.qty21 = request.POST.get('qty21')

            message = message + "21) " + neworder.line21.name + " : " + neworder.qty21 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line21.retailprice) + "\n"
            else:
                message = message + str(neworder.line21.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line21 = None
        try:
            neworder.line22 = Products.objects.get(pk=int(request.POST.get('option22')))
            neworder.qty22 = request.POST.get('qty22')

            message = message + "22) " + neworder.line22.name + " : " + neworder.qty22 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line22.retailprice) + "\n"
            else:
                message = message + str(neworder.line22.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line22 = None
        try:
            neworder.line23 = Products.objects.get(pk=int(request.POST.get('option23')))
            neworder.qty23 = request.POST.get('qty23')

            message = message + "23) " + neworder.line23.name + " : " + neworder.qty23 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line23.retailprice) + "\n"
            else:
                message = message + str(neworder.line23.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line23 = None
        try:
            neworder.line24 = Products.objects.get(pk=int(request.POST.get('option24')))
            neworder.qty24 = request.POST.get('qty24')

            message = message + "24) " + neworder.line24.name + " : " + neworder.qty24 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line24.retailprice) + "\n"
            else:
                message = message + str(neworder.line24.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line24 = None
        try:
            neworder.line25 = Products.objects.get(pk=int(request.POST.get('option25')))
            neworder.qty25 = request.POST.get('qty25')

            message = message + "25) " + neworder.line25.name + " : " + neworder.qty25 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line25.retailprice) + "\n"
            else:
                message = message + str(neworder.line25.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line25 = None
        try:
            neworder.line26 = Products.objects.get(pk=int(request.POST.get('option26')))
            neworder.qty26 = request.POST.get('qty26')

            message = message + "26) " + neworder.line26.name + " : " + neworder.qty26 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line26.retailprice) + "\n"
            else:
                message = message + str(neworder.line26.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line26 = None
        try:
            neworder.line27 = Products.objects.get(pk=int(request.POST.get('option27')))
            neworder.qty27 = request.POST.get('qty27')

            message = message + "27) " + neworder.line27.name + " : " + neworder.qty27 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line27.retailprice) + "\n"
            else:
                message = message + str(neworder.line27.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line27 = None
        try:
            neworder.line28 = Products.objects.get(pk=int(request.POST.get('option28')))
            neworder.qty28 = request.POST.get('qty28')

            message = message + "28) " + neworder.line28.name + " : " + neworder.qty28 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line28.retailprice) + "\n"
            else:
                message = message + str(neworder.line28.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line28 = None
        try:
            neworder.line29 = Products.objects.get(pk=int(request.POST.get('option29')))
            neworder.qty29 = request.POST.get('qty29')

            message = message + "29) " + neworder.line29.name + " : " + neworder.qty29 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line29.retailprice) + "\n"
            else:
                message = message + str(neworder.line29.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line29 = None
        try:
            neworder.line30 = Products.objects.get(pk=int(request.POST.get('option30')))
            neworder.qty30 = request.POST.get('qty30')

            message = message + "30) " + neworder.line30.name + " : " + neworder.qty30 + " x $" 
            if not request.user.is_authenticated or request.user.is_staff:
                message = message + str(neworder.line30.retailprice) + "\n"
            else:
                message = message + str(neworder.line30.unitprice) + "\n"
        except Products.DoesNotExist:
            neworder.line30 = None

        
            
        neworder.address = request.POST.get('address')
        neworder.prefferedtiming = request.POST.get("prefferedtime",None)
        neworder.preffereddate = request.POST.get("deliverydate")

        neworder.save()
        neworder = Orders.objects.annotate(sum1=Sum(Coalesce(F('line1__unitprice'),0)*F('qty1')+Coalesce(F('line2__unitprice'),0)*F('qty2')+Coalesce(F('line3__unitprice'),0)*F('qty3')+Coalesce(F('line4__unitprice'),0)*F('qty4')+Coalesce(F('line5__unitprice'),0)*F('qty5')+Coalesce(F('line6__unitprice'),0)*F('qty6')+Coalesce(F('line7__unitprice'),0)*F('qty7')+Coalesce(F('line8__unitprice'),0)*F('qty8')+Coalesce(F('line9__unitprice'),0)*F('qty9')+Coalesce(F('line10__unitprice'),0)*F('qty10')+Coalesce(F('line11__unitprice'),0)*F('qty11')+Coalesce(F('line12__unitprice'),0)*F('qty12')+Coalesce(F('line13__unitprice'),0)*F('qty13')+Coalesce(F('line14__unitprice'),0)*F('qty14')+Coalesce(F('line15__unitprice'),0)*F('qty15')+Coalesce(F('line16__unitprice'),0)*F('qty16')+Coalesce(F('line17__unitprice'),0)*F('qty17')+Coalesce(F('line18__unitprice'),0)*F('qty18')+Coalesce(F('line19__unitprice'),0)*F('qty19')+Coalesce(F('line20__unitprice'),0)*F('qty20')+Coalesce(F('line21__unitprice'),0)*F('qty21')+Coalesce(F('line22__unitprice'),0)*F('qty22')+Coalesce(F('line23__unitprice'),0)*F('qty23')+Coalesce(F('line24__unitprice'),0)*F('qty24')+Coalesce(F('line25__unitprice'),0)*F('qty25')+Coalesce(F('line26__unitprice'),0)*F('qty26')+Coalesce(F('line27__unitprice'),0)*F('qty27')+Coalesce(F('line28__unitprice'),0)*F('qty28')+Coalesce(F('line29__unitprice'),0)*F('qty29')+Coalesce(F('line30__unitprice'),0)*F('qty30'),output_field=FloatField()),sum2=Sum(Coalesce(F('line1__retailprice'),0)*F('qty1')+Coalesce(F('line2__retailprice'),0)*F('qty2')+Coalesce(F('line3__retailprice'),0)*F('qty3')+Coalesce(F('line4__retailprice'),0)*F('qty4')+Coalesce(F('line5__retailprice'),0)*F('qty5')+Coalesce(F('line6__retailprice'),0)*F('qty6')+Coalesce(F('line7__retailprice'),0)*F('qty7')+Coalesce(F('line8__retailprice'),0)*F('qty8')+Coalesce(F('line9__retailprice'),0)*F('qty9')+Coalesce(F('line10__retailprice'),0)*F('qty10')+Coalesce(F('line11__retailprice'),0)*F('qty11')+Coalesce(F('line12__retailprice'),0)*F('qty12')+Coalesce(F('line13__retailprice'),0)*F('qty13')+Coalesce(F('line14__retailprice'),0)*F('qty14')+Coalesce(F('line15__retailprice'),0)*F('qty15')+Coalesce(F('line16__retailprice'),0)*F('qty16')+Coalesce(F('line17__retailprice'),0)*F('qty17')+Coalesce(F('line18__retailprice'),0)*F('qty18')+Coalesce(F('line19__retailprice'),0)*F('qty19')+Coalesce(F('line20__retailprice'),0)*F('qty20')+Coalesce(F('line21__retailprice'),0)*F('qty21')+Coalesce(F('line22__retailprice'),0)*F('qty22')+Coalesce(F('line23__retailprice'),0)*F('qty23')+Coalesce(F('line24__retailprice'),0)*F('qty24')+Coalesce(F('line25__retailprice'),0)*F('qty25')+Coalesce(F('line26__retailprice'),0)*F('qty26')+Coalesce(F('line27__retailprice'),0)*F('qty27')+Coalesce(F('line28__retailprice'),0)*F('qty28')+Coalesce(F('line29__retailprice'),0)*F('qty29')+Coalesce(F('line30__retailprice'),0)*F('qty30'),output_field=FloatField())).latest('created_at')
        subject = 'Wahyu Brand: Your Order No. #' + str(neworder.pk)
        
        if not request.user.is_authenticated or request.user.is_staff:
            message = message + "Total Order Value = $" + str(neworder.sum2)
            message = message + "\n*Orders Value Below $200 will be charged $10.00 Delivery\nPayment will be cash on delivery. If you have any issues, please contact: +65 87171300\n"
        else:
            message = message + "Total Order Value = $" + str(neworder.sum1) + "\n"

        message = message + "\nThank you for the kind support! \n\nBest Regards\n\nWahyu Brand Sales Team\n52 International Road #03-06 Singapore 619626\nContact No: 87171300"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get('email'),"rafiq.wahyubrand@gmail.com"]
        send_mail( subject, message, email_from, recipient_list )
        
        return redirect('order_confirmed')
    else:
        content = {
            'title':"Wahyu Brand: Online Order Form",
            'categories' : category,
            'products' : products,
            'dist' : dist,
            'current_dist' : current_dist,
            'orders' : orders,
            'total_lineItems' : range(1,31)
        }
        return render(request,'main/order.html', content)
@staff_member_required    
def excel(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            input_excel = request.FILES['input_excel']
            book = xlrd.open_workbook(file_contents=input_excel.read())
            xlsheet = book.sheet_by_index(0)
            for x in range(6,49):
                product = Products()
                product.name =  xlsheet.cell_value(rowx=x,colx=0)
                product.barcode = xlsheet.cell_value(rowx=x,colx=8)
                product.carton_dimensions = str(xlsheet.cell_value(rowx=x,colx=10)) + " x " + str(xlsheet.cell_value(rowx=x,colx=11)) + " x " + str(xlsheet.cell_value(rowx=x,colx=12))
                product.carton_qty = xlsheet.cell_value(rowx=x,colx=17)
                product.carton_weight = xlsheet.cell_value(rowx=x,colx=13)
                product.subcategory = Subcategory.objects.get(name=xlsheet.cell_value(rowx=x,colx=7))
                product.dimensions = str(xlsheet.cell_value(rowx=x,colx=14)) + " x " + str(xlsheet.cell_value(rowx=x,colx=15)) + " x " + str(xlsheet.cell_value(rowx=x,colx=16))
                product.grossweight = xlsheet.cell_value(rowx=x,colx=2)
                product.imgpath = xlsheet.cell_value(rowx=x,colx=19)
                product.productdescription = xlsheet.cell_value(rowx=x,colx=9)
                product.remarks = xlsheet.cell_value(rowx=x,colx=18)
                product.retailprice = xlsheet.cell_value(rowx=x,colx=4)
                product.category = Category.objects.get(name=xlsheet.cell_value(rowx=x,colx=20))
                product.unitnetweight = xlsheet.cell_value(rowx=x,colx=1)
                product.unitprice = xlsheet.cell_value(rowx=x,colx=3)
                product.name2 =  xlsheet.cell_value(rowx=x,colx=21)
                product.save()
            return HttpResponseRedirect('/admin/')
    else:
        form = UploadFileForm()
    return render(request, 'main/excel.html', {'form': form})
@staff_member_required
def register(request):
	if request.method == 'POST' :
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			return redirect('index')
	else:
		form = UserCreationForm()
		context = {'form' : form}
		return render(request, 'registration/register.html', context)

@login_required
def supplier(request):
    distributor = Distributors.objects.filter(username__username=request.user)
    if request.user.is_staff:
        orders = Orders.objects.filter(distributor__username=request.user).annotate(sum1=Sum(Coalesce(F('line1__retailprice'),0)*F('qty1')+Coalesce(F('line2__retailprice'),0)*F('qty2')+Coalesce(F('line3__retailprice'),0)*F('qty3')+Coalesce(F('line4__retailprice'),0)*F('qty4')+Coalesce(F('line5__retailprice'),0)*F('qty5')+Coalesce(F('line6__retailprice'),0)*F('qty6')+Coalesce(F('line7__retailprice'),0)*F('qty7')+Coalesce(F('line8__retailprice'),0)*F('qty8')+Coalesce(F('line9__retailprice'),0)*F('qty9')+Coalesce(F('line10__retailprice'),0)*F('qty10')+Coalesce(F('line11__retailprice'),0)*F('qty11')+Coalesce(F('line12__retailprice'),0)*F('qty12')+Coalesce(F('line13__retailprice'),0)*F('qty13')+Coalesce(F('line14__retailprice'),0)*F('qty14')+Coalesce(F('line15__retailprice'),0)*F('qty15')+Coalesce(F('line16__retailprice'),0)*F('qty16')+Coalesce(F('line17__retailprice'),0)*F('qty17')+Coalesce(F('line18__retailprice'),0)*F('qty18')+Coalesce(F('line19__retailprice'),0)*F('qty19')+Coalesce(F('line20__retailprice'),0)*F('qty20')+Coalesce(F('line21__retailprice'),0)*F('qty21')+Coalesce(F('line22__retailprice'),0)*F('qty22')+Coalesce(F('line23__retailprice'),0)*F('qty23')+Coalesce(F('line24__retailprice'),0)*F('qty24')+Coalesce(F('line25__retailprice'),0)*F('qty25')+Coalesce(F('line26__retailprice'),0)*F('qty26')+Coalesce(F('line27__retailprice'),0)*F('qty27')+Coalesce(F('line28__retailprice'),0)*F('qty28')+Coalesce(F('line29__retailprice'),0)*F('qty29')+Coalesce(F('line30__retailprice'),0)*F('qty30'),output_field=FloatField()))
    else:
        orders = Orders.objects.filter(distributor__username=request.user).annotate(sum1=Sum(Coalesce(F('line1__unitprice'),0)*F('qty1')+Coalesce(F('line2__unitprice'),0)*F('qty2')+Coalesce(F('line3__unitprice'),0)*F('qty3')+Coalesce(F('line4__unitprice'),0)*F('qty4')+Coalesce(F('line5__unitprice'),0)*F('qty5')+Coalesce(F('line6__unitprice'),0)*F('qty6')+Coalesce(F('line7__unitprice'),0)*F('qty7')+Coalesce(F('line8__unitprice'),0)*F('qty8')+Coalesce(F('line9__unitprice'),0)*F('qty9')+Coalesce(F('line10__unitprice'),0)*F('qty10')+Coalesce(F('line11__unitprice'),0)*F('qty11')+Coalesce(F('line12__unitprice'),0)*F('qty12')+Coalesce(F('line13__unitprice'),0)*F('qty13')+Coalesce(F('line14__unitprice'),0)*F('qty14')+Coalesce(F('line15__unitprice'),0)*F('qty15')+Coalesce(F('line16__unitprice'),0)*F('qty16')+Coalesce(F('line17__unitprice'),0)*F('qty17')+Coalesce(F('line18__unitprice'),0)*F('qty18')+Coalesce(F('line19__unitprice'),0)*F('qty19')+Coalesce(F('line20__unitprice'),0)*F('qty20')+Coalesce(F('line21__unitprice'),0)*F('qty21')+Coalesce(F('line22__unitprice'),0)*F('qty22')+Coalesce(F('line23__unitprice'),0)*F('qty23')+Coalesce(F('line24__unitprice'),0)*F('qty24')+Coalesce(F('line25__unitprice'),0)*F('qty25')+Coalesce(F('line26__unitprice'),0)*F('qty26')+Coalesce(F('line27__unitprice'),0)*F('qty27')+Coalesce(F('line28__unitprice'),0)*F('qty28')+Coalesce(F('line29__unitprice'),0)*F('qty29')+Coalesce(F('line30__unitprice'),0)*F('qty30'),output_field=FloatField()))
    
    context = {
        'distributor' : distributor,
        'orders' : orders       
    }

    return render(request, 'main/supplier.html', context)


class OrderDetailView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            order = get_object_or_404(Orders.objects.annotate(sum1=Sum(Coalesce(F('line1__unitprice'),0)*F('qty1')+Coalesce(F('line2__unitprice'),0)*F('qty2')+Coalesce(F('line3__unitprice'),0)*F('qty3')+Coalesce(F('line4__unitprice'),0)*F('qty4')+Coalesce(F('line5__unitprice'),0)*F('qty5')+Coalesce(F('line6__unitprice'),0)*F('qty6')+Coalesce(F('line7__unitprice'),0)*F('qty7')+Coalesce(F('line8__unitprice'),0)*F('qty8')+Coalesce(F('line9__unitprice'),0)*F('qty9')+Coalesce(F('line10__unitprice'),0)*F('qty10')+Coalesce(F('line11__unitprice'),0)*F('qty11')+Coalesce(F('line12__unitprice'),0)*F('qty12')+Coalesce(F('line13__unitprice'),0)*F('qty13')+Coalesce(F('line14__unitprice'),0)*F('qty14')+Coalesce(F('line15__unitprice'),0)*F('qty15')+Coalesce(F('line16__unitprice'),0)*F('qty16')+Coalesce(F('line17__unitprice'),0)*F('qty17')+Coalesce(F('line18__unitprice'),0)*F('qty18')+Coalesce(F('line19__unitprice'),0)*F('qty19')+Coalesce(F('line20__unitprice'),0)*F('qty20')+Coalesce(F('line21__unitprice'),0)*F('qty21')+Coalesce(F('line22__unitprice'),0)*F('qty22')+Coalesce(F('line23__unitprice'),0)*F('qty23')+Coalesce(F('line24__unitprice'),0)*F('qty24')+Coalesce(F('line25__unitprice'),0)*F('qty25')+Coalesce(F('line26__unitprice'),0)*F('qty26')+Coalesce(F('line27__unitprice'),0)*F('qty27')+Coalesce(F('line28__unitprice'),0)*F('qty28')+Coalesce(F('line29__unitprice'),0)*F('qty29')+Coalesce(F('line30__unitprice'),0)*F('qty30'),output_field=FloatField()),sum2=Sum(Coalesce(F('line1__retailprice'),0)*F('qty1')+Coalesce(F('line2__retailprice'),0)*F('qty2')+Coalesce(F('line3__retailprice'),0)*F('qty3')+Coalesce(F('line4__retailprice'),0)*F('qty4')+Coalesce(F('line5__retailprice'),0)*F('qty5')+Coalesce(F('line6__retailprice'),0)*F('qty6')+Coalesce(F('line7__retailprice'),0)*F('qty7')+Coalesce(F('line8__retailprice'),0)*F('qty8')+Coalesce(F('line9__retailprice'),0)*F('qty9')+Coalesce(F('line10__retailprice'),0)*F('qty10')+Coalesce(F('line11__retailprice'),0)*F('qty11')+Coalesce(F('line12__retailprice'),0)*F('qty12')+Coalesce(F('line13__retailprice'),0)*F('qty13')+Coalesce(F('line14__retailprice'),0)*F('qty14')+Coalesce(F('line15__retailprice'),0)*F('qty15')+Coalesce(F('line16__retailprice'),0)*F('qty16')+Coalesce(F('line17__retailprice'),0)*F('qty17')+Coalesce(F('line18__retailprice'),0)*F('qty18')+Coalesce(F('line19__retailprice'),0)*F('qty19')+Coalesce(F('line20__retailprice'),0)*F('qty20')+Coalesce(F('line21__retailprice'),0)*F('qty21')+Coalesce(F('line22__retailprice'),0)*F('qty22')+Coalesce(F('line23__retailprice'),0)*F('qty23')+Coalesce(F('line24__retailprice'),0)*F('qty24')+Coalesce(F('line25__retailprice'),0)*F('qty25')+Coalesce(F('line26__retailprice'),0)*F('qty26')+Coalesce(F('line27__retailprice'),0)*F('qty27')+Coalesce(F('line28__retailprice'),0)*F('qty28')+Coalesce(F('line29__retailprice'),0)*F('qty29')+Coalesce(F('line30__retailprice'),0)*F('qty30'),output_field=FloatField())), pk=kwargs['pk'])
        else:
            order = get_object_or_404(Orders.objects.filter(distributor__username=request.user).annotate(sum1=Sum(Coalesce(F('line1__unitprice'),0)*F('qty1')+Coalesce(F('line2__unitprice'),0)*F('qty2')+Coalesce(F('line3__unitprice'),0)*F('qty3')+Coalesce(F('line4__unitprice'),0)*F('qty4')+Coalesce(F('line5__unitprice'),0)*F('qty5')+Coalesce(F('line6__unitprice'),0)*F('qty6')+Coalesce(F('line7__unitprice'),0)*F('qty7')+Coalesce(F('line8__unitprice'),0)*F('qty8')+Coalesce(F('line9__unitprice'),0)*F('qty9')+Coalesce(F('line10__unitprice'),0)*F('qty10')+Coalesce(F('line11__unitprice'),0)*F('qty11')+Coalesce(F('line12__unitprice'),0)*F('qty12')+Coalesce(F('line13__unitprice'),0)*F('qty13')+Coalesce(F('line14__unitprice'),0)*F('qty14')+Coalesce(F('line15__unitprice'),0)*F('qty15')+Coalesce(F('line16__unitprice'),0)*F('qty16')+Coalesce(F('line17__unitprice'),0)*F('qty17')+Coalesce(F('line18__unitprice'),0)*F('qty18')+Coalesce(F('line19__unitprice'),0)*F('qty19')+Coalesce(F('line20__unitprice'),0)*F('qty20')+Coalesce(F('line21__unitprice'),0)*F('qty21')+Coalesce(F('line22__unitprice'),0)*F('qty22')+Coalesce(F('line23__unitprice'),0)*F('qty23')+Coalesce(F('line24__unitprice'),0)*F('qty24')+Coalesce(F('line25__unitprice'),0)*F('qty25')+Coalesce(F('line26__unitprice'),0)*F('qty26')+Coalesce(F('line27__unitprice'),0)*F('qty27')+Coalesce(F('line28__unitprice'),0)*F('qty28')+Coalesce(F('line29__unitprice'),0)*F('qty29')+Coalesce(F('line30__unitprice'),0)*F('qty30'),output_field=FloatField())), pk=kwargs['pk'])           
        context = {
            'order': order,
            'total_lineItems' : range(1,31)
                }
        return render(request, 'main/order_detail.html', context)

@staff_member_required
def orders(request, year=None, month=None, day=None, pk=None, update=None):

    distributor = Distributors.objects.filter(username__username=request.user)
    
    if request.method == 'POST' :    
        # response content type
        response = HttpResponse(content_type='text/csv')
        #decide the file name
        response['Content-Disposition'] = 'attachment; filename="Transaksi.csv"'

        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))

        #write the headers
        writer.writerow([
            smart_str(u"No. Invoice"),
            smart_str(u"factur"),
            smart_str(u"Tanggal Transaksi"),
            smart_str(u"Kode Customer"),
            smart_str(u"Nama Customer"),
            smart_str(u"Kode Barang"),
            smart_str(u"Nama Barang"),
            smart_str(u"size"),
            smart_str(u"Type Harga Jual"),
            smart_str(u"Quantity"),
            smart_str(u"Harga"),
            smart_str(u"Type Transaksi"),
            smart_str(u"User"),
            smart_str(u"Tgl. Entry"),
            smart_str(u"Jam Entry"),
            smart_str(u"Total"),
            smart_str(u"Remark"),
            smart_str(u"No. DO"),
            smart_str(u"UOM"),
            smart_str(u"Tgl. Jatuh Tempo"),
            smart_str(u"Term"),
            smart_str(u"Kategori"),
            smart_str(u"Tgl. Order"),
            smart_str(u"Tgl. Delivery"),
            smart_str(u"Kode. Delivery"),
            smart_str(u"Nama Penerima"),
            smart_str(u"No. PO"),
        ])
        #get data from database or from text file....
        orders = Orders.objects.all().annotate(sum1=Sum(Coalesce(F('line1__unitprice'),0)*F('qty1')+Coalesce(F('line2__unitprice'),0)*F('qty2')+Coalesce(F('line3__unitprice'),0)*F('qty3')+Coalesce(F('line4__unitprice'),0)*F('qty4')+Coalesce(F('line5__unitprice'),0)*F('qty5')+Coalesce(F('line6__unitprice'),0)*F('qty6')+Coalesce(F('line7__unitprice'),0)*F('qty7')+Coalesce(F('line8__unitprice'),0)*F('qty8')+Coalesce(F('line9__unitprice'),0)*F('qty9')+Coalesce(F('line10__unitprice'),0)*F('qty10')+Coalesce(F('line11__unitprice'),0)*F('qty11')+Coalesce(F('line12__unitprice'),0)*F('qty12')+Coalesce(F('line13__unitprice'),0)*F('qty13')+Coalesce(F('line14__unitprice'),0)*F('qty14')+Coalesce(F('line15__unitprice'),0)*F('qty15')+Coalesce(F('line16__unitprice'),0)*F('qty16')+Coalesce(F('line17__unitprice'),0)*F('qty17')+Coalesce(F('line18__unitprice'),0)*F('qty18')+Coalesce(F('line19__unitprice'),0)*F('qty19')+Coalesce(F('line20__unitprice'),0)*F('qty20')+Coalesce(F('line21__unitprice'),0)*F('qty21')+Coalesce(F('line22__unitprice'),0)*F('qty22')+Coalesce(F('line23__unitprice'),0)*F('qty23')+Coalesce(F('line24__unitprice'),0)*F('qty24')+Coalesce(F('line25__unitprice'),0)*F('qty25')+Coalesce(F('line26__unitprice'),0)*F('qty26')+Coalesce(F('line27__unitprice'),0)*F('qty27')+Coalesce(F('line28__unitprice'),0)*F('qty28')+Coalesce(F('line29__unitprice'),0)*F('qty29')+Coalesce(F('line30__unitprice'),0)*F('qty30'),output_field=FloatField())) #dummy function to fetch data
        var = request.POST.getlist('pickupcheck[]')
        invoiceno = int(request.POST.get('invoice')) + 1
        ponum = int(request.POST.get('ponum')) + 1
        for order in orders:
            invoice = "WA" + str(invoiceno).zfill(5) + "/INV/VI/2015"
            if str(order.pk) in var:
                if order.line1 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line1.productcode),
                        smart_str(order.line1.name),
                        smart_str(order.line1.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty1),
                        smart_str(order.line1.unitprice if order.distributor.name != "Direct Sales" else order.line1.retailprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line1_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line1.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line2 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line2.productcode),
                        smart_str(order.line2.name),
                        smart_str(order.line2.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty2),
                        smart_str(order.line2.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line2_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line2.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line3 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line3.productcode),
                        smart_str(order.line3.name),
                        smart_str(order.line3.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty3),
                        smart_str(order.line3.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line3_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line3.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line4 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line4.productcode),
                        smart_str(order.line4.name),
                        smart_str(order.line4.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty4),
                        smart_str(order.line4.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line4_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line4.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line5 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line5.productcode),
                        smart_str(order.line5.name),
                        smart_str(order.line5.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty5),
                        smart_str(order.line5.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line5_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line5.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line6 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line6.productcode),
                        smart_str(order.line6.name),
                        smart_str(order.line6.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty6),
                        smart_str(order.line6.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line6_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line6.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line7 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line7.productcode),
                        smart_str(order.line7.name),
                        smart_str(order.line7.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty7),
                        smart_str(order.line7.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line7_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line7.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line8 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line8.productcode),
                        smart_str(order.line8.name),
                        smart_str(order.line8.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty8),
                        smart_str(order.line8.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line8_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line8.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line9 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line9.productcode),
                        smart_str(order.line9.name),
                        smart_str(order.line9.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty9),
                        smart_str(order.line9.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line9_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line9.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line10 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line10.productcode),
                        smart_str(order.line10.name),
                        smart_str(order.line10.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty10),
                        smart_str(order.line10.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line10_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line10.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line11 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line11.productcode),
                        smart_str(order.line11.name),
                        smart_str(order.line11.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty11),
                        smart_str(order.line11.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line11_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line11.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line12 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line12.productcode),
                        smart_str(order.line12.name),
                        smart_str(order.line12.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty12),
                        smart_str(order.line12.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line12_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line12.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line13 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line13.productcode),
                        smart_str(order.line13.name),
                        smart_str(order.line13.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty13),
                        smart_str(order.line13.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line13_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line13.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line14 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line14.productcode),
                        smart_str(order.line14.name),
                        smart_str(order.line14.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty14),
                        smart_str(order.line14.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line14_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line14.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line15 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line15.productcode),
                        smart_str(order.line15.name),
                        smart_str(order.line15.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty15),
                        smart_str(order.line15.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line15_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line15.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line16 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line16.productcode),
                        smart_str(order.line16.name),
                        smart_str(order.line16.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty16),
                        smart_str(order.line16.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line16_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line16.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line17 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line17.productcode),
                        smart_str(order.line17.name),
                        smart_str(order.line17.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty17),
                        smart_str(order.line17.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line17_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line17.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line18 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line18.productcode),
                        smart_str(order.line18.name),
                        smart_str(order.line18.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty18),
                        smart_str(order.line18.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line18_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line18.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line19 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line19.productcode),
                        smart_str(order.line19.name),
                        smart_str(order.line19.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty19),
                        smart_str(order.line19.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line19_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line19.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line20 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line20.productcode),
                        smart_str(order.line20.name),
                        smart_str(order.line20.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty20),
                        smart_str(order.line20.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line20_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line20.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line21 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line21.productcode),
                        smart_str(order.line21.name),
                        smart_str(order.line21.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty21),
                        smart_str(order.line21.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line21_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line21.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line22 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line22.productcode),
                        smart_str(order.line22.name),
                        smart_str(order.line22.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty22),
                        smart_str(order.line22.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line22_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line22.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line23 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line23.productcode),
                        smart_str(order.line23.name),
                        smart_str(order.line23.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty23),
                        smart_str(order.line23.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line23_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line23.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line24 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line24.productcode),
                        smart_str(order.line24.name),
                        smart_str(order.line24.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty24),
                        smart_str(order.line24.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line24_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line24.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line25 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line25.productcode),
                        smart_str(order.line25.name),
                        smart_str(order.line25.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty25),
                        smart_str(order.line25.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line25_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line25.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line26 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line26.productcode),
                        smart_str(order.line26.name),
                        smart_str(order.line26.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty26),
                        smart_str(order.line26.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line26_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line26.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line27 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line27.productcode),
                        smart_str(order.line27.name),
                        smart_str(order.line27.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty27),
                        smart_str(order.line27.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line27_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line27.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line28 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line28.productcode),
                        smart_str(order.line28.name),
                        smart_str(order.line28.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty28),
                        smart_str(order.line28.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line28_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line28.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line29 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line29.productcode),
                        smart_str(order.line29.name),
                        smart_str(order.line29.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty29),
                        smart_str(order.line29.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line29_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line29.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.line30 != None:
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.distributor.name if order.distributor.name != "Direct Sales" else order.name),
                        smart_str(order.line30.productcode),
                        smart_str(order.line30.name),
                        smart_str(order.line30.unitnetweight),
                        smart_str("Selling Pr" if order.distributor.name != "Direct Sales" else "Market Pr"),
                        smart_str(order.qty30),
                        smart_str(order.line30.unitprice),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str(order.line30_total()),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str(order.line30.category),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                if order.sum1 < 200 and order.distributor.name == "Direct Sales" :
                    writer.writerow([
                        smart_str(invoice),
                        smart_str(""),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(order.distributor.distributorcode),
                        smart_str(order.name),
                        smart_str("Del"),
                        smart_str("Delivery Charge"),
                        smart_str("0"),
                        smart_str("Market Pr"),
                        smart_str("1"),
                        smart_str("10"),
                        smart_str("JP"),
                        smart_str(""),
                        smart_str("/ /"),
                        smart_str(""),
                        smart_str("10"),
                        smart_str(""),
                        smart_str(""),
                        smart_str("Can"),
                        smart_str("/ /"),
                        smart_str(order.distributor.paymentterms),
                        smart_str("Delivery"),
                        smart_str(order.created_at.strftime("%d/%m/%Y")),
                        smart_str(datetime.strptime(order.preffereddate,"%b %d, %Y").strftime("%d/%m/%Y")),
                        smart_str("2"),
                        smart_str("PUTHI"),
                        smart_str(ponum),
                    ])
                
                ponum = ponum + 1
                invoiceno = invoiceno + 1
        return response
    else:
        if update == "pickup" and pk !=None:
            updateorder = Orders.objects.get(pk=pk)
            #print(str(updateorder.pickuptime) + " " + str(updateorder.created_at))
            if updateorder.pickuptime.strftime("%m/%d/%Y, %H:%M:%S") == updateorder.created_at.strftime("%m/%d/%Y, %H:%M:%S"):
                updateorder.pickuptime = datetime.now()
                #print("updateorder.pickuptime == updateorder.created_at")
            else:
                updateorder.pickuptime = updateorder.created_at
                #print("NOT updateorder.pickuptime == updateorder.created_at")
            updateorder.save()
            time = datetime.strptime(updateorder.preffereddate,"%b %d, %Y")
            not_today = True
        elif update == "deliver" and pk !=None:
            updateorder = Orders.objects.get(pk=pk)
            if updateorder.deliveredtime.strftime("%m/%d/%Y, %H:%M:%S") == updateorder.created_at.strftime("%m/%d/%Y, %H:%M:%S"):
                updateorder.deliveredtime = datetime.now()
            else:
                updateorder.deliveredtime = updateorder.created_at
            updateorder.save()
            time = datetime.strptime(updateorder.preffereddate,"%b %d, %Y")
            not_today = True
        elif update == "cash" and pk !=None:
            updateorder = Orders.objects.get(pk=pk)
            if updateorder.cashtime.strftime("%m/%d/%Y, %H:%M:%S") == updateorder.created_at.strftime("%m/%d/%Y, %H:%M:%S"):
                updateorder.cashtime = datetime.now()
            else:
                updateorder.cashtime = updateorder.created_at
            updateorder.save()
            time = datetime.strptime(updateorder.preffereddate,"%b %d, %Y")
            not_today = True
        elif update == "confirm" and pk !=None:
            updateorder = Orders.objects.get(pk=pk)
            #print(str(updateorder.cashconfirmtime) + " " + str(updateorder.created_at))
            if updateorder.cashconfirmtime.strftime("%m/%d/%Y, %H:%M:%S") == updateorder.created_at.strftime("%m/%d/%Y, %H:%M:%S"):
                updateorder.cashconfirmtime = datetime.now()
                #print("updateorder.pickuptime == updateorder.created_at")
            else:
                updateorder.cashconfirmtime = updateorder.created_at
                #print("NOT updateorder.pickuptime == updateorder.created_at")
            updateorder.save()
            time = datetime.strptime(updateorder.preffereddate,"%b %d, %Y")
            not_today = True
        elif year == None or month == None or day == None:
            time = datetime.now()
            not_today = False
        else:
            time = datetime(year=year,month=month,day=day)
            not_today = True

        orders = Orders.objects.filter(preffereddate=time.strftime("%b %d, %Y")).annotate(sum1=Sum(Coalesce(F('line1__unitprice'),0)*F('qty1')+Coalesce(F('line2__unitprice'),0)*F('qty2')+Coalesce(F('line3__unitprice'),0)*F('qty3')+Coalesce(F('line4__unitprice'),0)*F('qty4')+Coalesce(F('line5__unitprice'),0)*F('qty5')+Coalesce(F('line6__unitprice'),0)*F('qty6')+Coalesce(F('line7__unitprice'),0)*F('qty7')+Coalesce(F('line8__unitprice'),0)*F('qty8')+Coalesce(F('line9__unitprice'),0)*F('qty9')+Coalesce(F('line10__unitprice'),0)*F('qty10')+Coalesce(F('line11__unitprice'),0)*F('qty11')+Coalesce(F('line12__unitprice'),0)*F('qty12')+Coalesce(F('line13__unitprice'),0)*F('qty13')+Coalesce(F('line14__unitprice'),0)*F('qty14')+Coalesce(F('line15__unitprice'),0)*F('qty15')+Coalesce(F('line16__unitprice'),0)*F('qty16')+Coalesce(F('line17__unitprice'),0)*F('qty17')+Coalesce(F('line18__unitprice'),0)*F('qty18')+Coalesce(F('line19__unitprice'),0)*F('qty19')+Coalesce(F('line20__unitprice'),0)*F('qty20')+Coalesce(F('line21__unitprice'),0)*F('qty21')+Coalesce(F('line22__unitprice'),0)*F('qty22')+Coalesce(F('line23__unitprice'),0)*F('qty23')+Coalesce(F('line24__unitprice'),0)*F('qty24')+Coalesce(F('line25__unitprice'),0)*F('qty25')+Coalesce(F('line26__unitprice'),0)*F('qty26')+Coalesce(F('line27__unitprice'),0)*F('qty27')+Coalesce(F('line28__unitprice'),0)*F('qty28')+Coalesce(F('line29__unitprice'),0)*F('qty29')+Coalesce(F('line30__unitprice'),0)*F('qty30'),output_field=FloatField()),sum2=Sum(Coalesce(F('line1__retailprice'),0)*F('qty1')+Coalesce(F('line2__retailprice'),0)*F('qty2')+Coalesce(F('line3__retailprice'),0)*F('qty3')+Coalesce(F('line4__retailprice'),0)*F('qty4')+Coalesce(F('line5__retailprice'),0)*F('qty5')+Coalesce(F('line6__retailprice'),0)*F('qty6')+Coalesce(F('line7__retailprice'),0)*F('qty7')+Coalesce(F('line8__retailprice'),0)*F('qty8')+Coalesce(F('line9__retailprice'),0)*F('qty9')+Coalesce(F('line10__retailprice'),0)*F('qty10')+Coalesce(F('line11__retailprice'),0)*F('qty11')+Coalesce(F('line12__retailprice'),0)*F('qty12')+Coalesce(F('line13__retailprice'),0)*F('qty13')+Coalesce(F('line14__retailprice'),0)*F('qty14')+Coalesce(F('line15__retailprice'),0)*F('qty15')+Coalesce(F('line16__retailprice'),0)*F('qty16')+Coalesce(F('line17__retailprice'),0)*F('qty17')+Coalesce(F('line18__retailprice'),0)*F('qty18')+Coalesce(F('line19__retailprice'),0)*F('qty19')+Coalesce(F('line20__retailprice'),0)*F('qty20')+Coalesce(F('line21__retailprice'),0)*F('qty21')+Coalesce(F('line22__retailprice'),0)*F('qty22')+Coalesce(F('line23__retailprice'),0)*F('qty23')+Coalesce(F('line24__retailprice'),0)*F('qty24')+Coalesce(F('line25__retailprice'),0)*F('qty25')+Coalesce(F('line26__retailprice'),0)*F('qty26')+Coalesce(F('line27__retailprice'),0)*F('qty27')+Coalesce(F('line28__retailprice'),0)*F('qty28')+Coalesce(F('line29__retailprice'),0)*F('qty29')+Coalesce(F('line30__retailprice'),0)*F('qty30'),output_field=FloatField()))

        context = {
            'distributor' : distributor,
            'orders' : orders,
            'time': time,      
            'not_today': not_today
        }

    return render(request, 'main/orders.html', context)

def order_confirmed(request):
    context = {

    }

    return render(request, 'main/order_confirmed.html',context)

def supplier_register(request):

    if request.method == 'POST':
        subject = 'Wahyu Brand New Wholesaler Account Request'
        message = "Company Name:\n" + request.POST.get('companyname') + "\nCompany Address\n" + request.POST.get('CompanyAddress') + "\nContact Name:\n" + request.POST.get('ContactName') + "\nContact No:\n" + request.POST.get('ContactNo')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get('email'),"rafiq.wahyubrand@gmail.com"]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('index')
    else:
        context = {

        }

        return render(request, 'main/supplier_registration.html',context)