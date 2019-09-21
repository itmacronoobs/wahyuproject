from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime 
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Category(models.Model): #Paste, Sambal, Rempeyek *Product Line
 name = models.CharField(max_length=200)
 description = models.TextField()
 def __str__(self):
     return self.name

 class Meta:
  verbose_name_plural = "Category"

class Subcategory (models.Model): #Foodservice or Retail *Product Width
 name = models.CharField(max_length=200)
 def __str__(self):
    return self.name

 class Meta:
  verbose_name_plural = "Sub Category"

class Products (models.Model): #Products Details
    productcode = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=200)
    unitnetweight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    grossweight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    unitprice = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    retailprice = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)]) 
    productdescription = models.TextField(max_length=200)
    dimensions = models.CharField(max_length=200)
    carton_weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)]) 
    carton_dimensions = models.CharField(max_length=200)
    carton_qty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    remarks = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    imgpath = models.TextField(max_length=200)
    def __str__(self):
        return self.name

    class Meta:
      verbose_name_plural = "Product"

class Discounts (models.Model): #Discounts for customers *Routers
    name = models.CharField(max_length=200)
    discount_given = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    def __str__(self):
     return self.name

    class Meta:
     verbose_name_plural = "Discount"

class ship2(models.Model):
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=200)

    class Meta:
      verbose_name_plural = "ship2"



class Distributors (models.Model): #Wholesalers Details
    distributorcode = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    bill2contact_number = models.CharField(max_length=20)
    bill2address = models.TextField()
    ship2address =  models.ForeignKey(ship2, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discounts, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    paymentterms = models.CharField(max_length=200)
        
    def __str__(self):
      return self.name
    class Meta:
           verbose_name_plural = "Distributor"

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#   if created:
#        Distributors.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()

    
class Reviews(models.Model):
    name = models.CharField(max_length=200)
    productname = models.ForeignKey(Products, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
     return self.title

    class Meta:
      verbose_name_plural = "Review"

class Tag(models.Model):
    tag = models.CharField(max_length=200)
    def _str_(self):
     return self.tag

    class Meta:
     verbose_name_plural = "Tag"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    created_by = models.CharField(max_length=200)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    imgpath = models.TextField(max_length=200)
    def _str_(self):
     return self.title

     class Meta:
      verbose_name_plural = "Blog"

class Customers(models.Model): #Product Quality Customers *for main website
    name = models.CharField(max_length=200)
    imgpath = models.TextField(max_length=200)
    def _str_(self):
     return self.title

    class Meta:
     verbose_name_plural = "Customer"

class Orders(models.Model):
    orderno = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    invoiceno = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    contactno = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True, null= True)
    distributor = models.ForeignKey(Distributors, on_delete=models.CASCADE)

    line1= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item1")
    line2= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item2")
    line3= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item3")
    line4= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item4")
    line5= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item5")
    line6= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item6")
    line7= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item7")
    line8= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item8")
    line9= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item9")
    line10= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item10")
    line11= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item11")
    line12= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item12")
    line13= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item13")
    line14= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item14")
    line15= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item15")
    line16= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item16")
    line17= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item17")
    line18= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item18")
    line19= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item19")
    line20= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item20")
    line21= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item21")
    line22= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item22")
    line23= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item23")
    line24= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item24")
    line25= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item25")
    line26= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item26")
    line27= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item27")
    line28= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item28")
    line29= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item29")
    line30= models.ForeignKey(Products, on_delete=models.CASCADE, related_name="line_item30" )

    qty1= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty2= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty3= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty4= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty5= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty6= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty7= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty8= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty9= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty10= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty11= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty12= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty13= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty14= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty15= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty16= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty17= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty18= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty19= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty20= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty21= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty22= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty23= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty24= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty25= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty26= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty27= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty28= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty29= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    qty30= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])

    address= models.CharField(max_length=200)
    prefferedtiming = models.CharField(max_length=200)
    preffereddate = models.CharField(max_length=200)
    pickuptime = models.DateTimeField(default=datetime.now, blank=True)
    deliveredtime = models.DateTimeField(default=datetime.now, blank=True)
    cashtime = models.DateTimeField(default=datetime.now, blank=True)
    cashconfirmtime = models.DateTimeField(default=datetime.now, blank=True)

    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    class Meta:
      verbose_name_plural = "Order"