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

    content = {
        'title':"Wahyu Brand: Online Order Form",
        'categories' : category,
        'products' : products,
        'dist' : dist,
        'orders' : orders
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