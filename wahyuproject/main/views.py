from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .models import Products, Category, Subcategory, Distributors, User, Orders
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

import xlrd

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
    orders = Orders.objects.all

    if request.method == 'POST':
        neworder = Orders()
        neworder.orderno = "123456"
        neworder.name = request.POST.get("name")
        neworder.contactno = request.POST.get("contactno")
        neworder.email = request.POST.get("email")
        neworder.distributor = Distributors.objects.get(username=request.user)
        try:
            neworder.line1 = Products.objects.get(pk=int(request.POST.get("option1")))
        except Products.DoesNotExist:
            neworder.line1 = None
        try:
            neworder.line2 = Products.objects.get(pk=int(request.POST.get("option2")))
        except Products.DoesNotExist:
            neworder.line2 = None
        try:
            neworder.line3 = Products.objects.get(pk=int(request.POST.get('option3')))
        except Products.DoesNotExist:
            neworder.line3 = None
        try:
            neworder.line4 = Products.objects.get(pk=int(request.POST.get('option4')))
        except Products.DoesNotExist:
            neworder.line4 = None
        try:
            neworder.line5 = Products.objects.get(pk=int(request.POST.get('option5')))
        except Products.DoesNotExist:
            neworder.line5 = None
        try:
            neworder.line6 = Products.objects.get(pk=int(request.POST.get('option6')))
        except Products.DoesNotExist:
            neworder.line6 = None
        try:
            neworder.line7 = Products.objects.get(pk=int(request.POST.get('option7')))
        except Products.DoesNotExist:
            neworder.line7 = None
        try:
            neworder.line8 = Products.objects.get(pk=int(request.POST.get('option8')))
        except Products.DoesNotExist:
            neworder.line8 = None
        try:
            neworder.line9 = Products.objects.get(pk=int(request.POST.get('option9')))
        except Products.DoesNotExist:
            neworder.line9 = None
        try:
            neworder.line10 = Products.objects.get(pk=int(request.POST.get('option10')))
        except Products.DoesNotExist:
            neworder.line10 = None 
        try:      
            neworder.line11 = Products.objects.get(pk=int(request.POST.get('option11')))
        except Products.DoesNotExist:
            neworder.line11 = None
        try:
            neworder.line12 = Products.objects.get(pk=int(request.POST.get('option12')))
        except Products.DoesNotExist:
            neworder.line12 = None
        try:
            neworder.line13 = Products.objects.get(pk=int(request.POST.get('option13')))
        except Products.DoesNotExist:
            neworder.line13 = None
        try:
            neworder.line14 = Products.objects.get(pk=int(request.POST.get('option14')))
        except Products.DoesNotExist:
            neworder.line14 = None
        try:
            neworder.line15 = Products.objects.get(pk=int(request.POST.get('option15')))
        except Products.DoesNotExist:
            neworder.line15 = None
        try:
            neworder.line16 = Products.objects.get(pk=int(request.POST.get('option16')))
        except Products.DoesNotExist:
            neworder.line16 = None
        try:
            neworder.line17 = Products.objects.get(pk=int(request.POST.get('option17')))
        except Products.DoesNotExist:
            neworder.line17 = None
        try:
            neworder.line18 = Products.objects.get(pk=int(request.POST.get('option18')))
        except Products.DoesNotExist:
            neworder.line18 = None
        try:
            neworder.line19 = Products.objects.get(pk=int(request.POST.get('option19')))
        except Products.DoesNotExist:
            neworder.line19 = None
        try:
            neworder.line20 = Products.objects.get(pk=int(request.POST.get('option20')))
        except Products.DoesNotExist:
            neworder.line20 = None
        try:
            neworder.line21 = Products.objects.get(pk=int(request.POST.get('option21')))
        except Products.DoesNotExist:
            neworder.line21 = None
        try:
            neworder.line22 = Products.objects.get(pk=int(request.POST.get('option22')))
        except Products.DoesNotExist:
            neworder.line22 = None
        try:
            neworder.line23 = Products.objects.get(pk=int(request.POST.get('option23')))
        except Products.DoesNotExist:
            neworder.line23 = None
        try:
            neworder.line24 = Products.objects.get(pk=int(request.POST.get('option24')))
        except Products.DoesNotExist:
            neworder.line24 = None
        try:
            neworder.line25 = Products.objects.get(pk=int(request.POST.get('option25')))
        except Products.DoesNotExist:
            neworder.line25 = None
        try:
            neworder.line26 = Products.objects.get(pk=int(request.POST.get('option26')))
        except Products.DoesNotExist:
            neworder.line26 = None
        try:
            neworder.line27 = Products.objects.get(pk=int(request.POST.get('option27')))
        except Products.DoesNotExist:
            neworder.line27 = None
        try:
            neworder.line28 = Products.objects.get(pk=int(request.POST.get('option28')))
        except Products.DoesNotExist:
            neworder.line28 = None
        try:
            neworder.line29 = Products.objects.get(pk=int(request.POST.get('option29')))
        except Products.DoesNotExist:
            neworder.line29 = None
        try:
            neworder.line30 = Products.objects.get(pk=int(request.POST.get('option30')))
        except Products.DoesNotExist:
            neworder.line30 = None
        

        neworder.qty1 = request.POST.get('qty1')
        neworder.qty2 = request.POST.get('qty2')
        neworder.qty3 = request.POST.get('qty3')
        neworder.qty4 = request.POST.get('qty4')
        neworder.qty5 = request.POST.get('qty5')
        neworder.qty6 = request.POST.get('qty6')
        neworder.qty7 = request.POST.get('qty7')
        neworder.qty8 = request.POST.get('qty8')
        neworder.qty9 = request.POST.get('qty9')
        neworder.qty10 = request.POST.get('qty10')
        neworder.qty11 = request.POST.get('qty11')
        neworder.qty12 = request.POST.get('qty12')
        neworder.qty13 = request.POST.get('qty13')
        neworder.qty14 = request.POST.get('qty14')
        neworder.qty15 = request.POST.get('qty15')
        neworder.qty16 = request.POST.get('qty16')
        neworder.qty17 = request.POST.get('qty17')
        neworder.qty18 = request.POST.get('qty18')
        neworder.qty19 = request.POST.get('qty19')
        neworder.qty20 = request.POST.get('qty20')
        neworder.qty21 = request.POST.get('qty21')
        neworder.qty22 = request.POST.get('qty22')
        neworder.qty23 = request.POST.get('qty23')
        neworder.qty24 = request.POST.get('qty24')
        neworder.qty25 = request.POST.get('qty25')
        neworder.qty26 = request.POST.get('qty26')
        neworder.qty27 = request.POST.get('qty27')
        neworder.qty28 = request.POST.get('qty28')
        neworder.qty29 = request.POST.get('qty29')
        neworder.qty30 = request.POST.get('qty30')

        neworder.address = request.POST.get('address')
        neworder.prefferedtiming = request.POST.get("prefferedtime",None)
        neworder.preffereddate = request.POST.get("deliverydate")

        neworder.save()

        return redirect('index')
    else:
        content = {
            'title':"Wahyu Brand: Online Order Form",
            'categories' : category,
            'products' : products,
            'dist' : dist,
            'orders' : orders,
            'total_lineItems' : range(1,31)
        }
        return render(request,'main/order.html', content)
    
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

def supplier(request):
    distributor = Distributors.objects.all
    orders = Orders.objects.all

    context = {
        'distributor' : distributor,
        'order' : orders       
    }

    return render(request, 'main/supplier.html', context)