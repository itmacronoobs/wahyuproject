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
    unitprice = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    retailprice = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(100)]) 
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

    def __str__(self):
      return self.address

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
     return self.name

    class Meta:
     verbose_name_plural = "Customer"

class Orders(models.Model):
    orderno = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    invoiceno = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    contactno = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True, null= True)
    distributor = models.ForeignKey(Distributors, on_delete=models.CASCADE)

    line1= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item1")
    line2= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item2")
    line3= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item3")
    line4= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item4")
    line5= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item5")
    line6= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item6")
    line7= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item7")
    line8= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item8")
    line9= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item9")
    line10= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item10")
    line11= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item11")
    line12= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item12")
    line13= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item13")
    line14= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item14")
    line15= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item15")
    line16= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item16")
    line17= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item17")
    line18= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item18")
    line19= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item19")
    line20= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item20")
    line21= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item21")
    line22= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item22")
    line23= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item23")
    line24= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item24")
    line25= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item25")
    line26= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item26")
    line27= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item27")
    line28= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item28")
    line29= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item29")
    line30= models.ForeignKey(Products, null=True, blank=True,  on_delete=models.CASCADE, related_name="line_item30" )

    qty1= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)],default=0)
    qty2= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)],default=0)
    qty3= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)],default=0)
    qty4= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)],default=0)
    qty5= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)],default=0)
    qty6= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty7= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty8= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty9= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty10= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty11= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty12= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty13= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty14= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty15= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty16= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty17= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty18= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty19= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty20= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty21= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty22= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty23= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty24= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty25= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty26= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty27= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty28= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty29= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    qty30= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)

    address= models.CharField(max_length=200)
    prefferedtiming = models.CharField(max_length=200)
    preffereddate = models.CharField(max_length=200)
    pickuptime = models.DateTimeField(default=datetime.now, blank=True)
    deliveredtime = models.DateTimeField(default=datetime.now, blank=True)
    cashtime = models.DateTimeField(default=datetime.now, blank=True)
    cashconfirmtime = models.DateTimeField(default=datetime.now, blank=True)

    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def line1_total(self):
        return self.line1.unitprice * self.qty1
    
    def line2_total(self):
        return self.line2.unitprice * self.qty2
    
    def line3_total(self):
        return self.line3.unitprice * self.qty3
    
    def line4_total(self):
        return self.line4.unitprice * self.qty4

    def line5_total(self):
        return self.line5.unitprice * self.qty5

    def line6_total(self):
        return self.line6.unitprice * self.qty6
    def line7_total(self):
        return self.line7.unitprice * self.qty7
    def line8_total(self):
        return self.line8.unitprice * self.qty8
    def line9_total(self):
        return self.line9.unitprice * self.qty9
    def line10_total(self):
        return self.line10.unitprice * self.qty10
    def line11_total(self):
        return self.line11.unitprice * self.qty11
    def line12_total(self):
        return self.line12.unitprice * self.qty12
    def line13_total(self):
        return self.line13.unitprice * self.qty13
    def line14_total(self):
        return self.line14.unitprice * self.qty14
    def line15_total(self):
        return self.line15.unitprice * self.qty15
    def line16_total(self):
        return self.line16.unitprice * self.qty16
    def line17_total(self):
        return self.line17.unitprice * self.qty17
    def line18_total(self):
        return self.line18.unitprice * self.qty18
    def line19_total(self):
        return self.line19.unitprice * self.qty19
    def line20_total(self):
        return self.line20.unitprice * self.qty20
    def line21_total(self):
        return self.line21.unitprice * self.qty21
    def line22_total(self):
        return self.line22.unitprice * self.qty22
    def line23_total(self):
        return self.line23.unitprice * self.qty23
    def line24_total(self):
        return self.line24.unitprice * self.qty24
    def line25_total(self):
        return self.line25.unitprice * self.qty25
    def line26_total(self):
        return self.line26.unitprice * self.qty26
    def line27_total(self):
        return self.line27.unitprice * self.qty27
    def line28_total(self):
        return self.line28.unitprice * self.qty28
    def line29_total(self):
        return self.line29.unitprice * self.qty29
    def line30_total(self):
        return self.line30.unitprice * self.qty30

    class Meta:
      verbose_name_plural = "Order"
