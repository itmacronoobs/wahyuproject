from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
	url(r'^$', views.index, name= 'index'),
	url(r'main', views.index, name= 'main'),
	url(r'excel', views.excel, name= 'excel'),
	url(r'^order$', views.order, name= 'order'),
	url(r'^order_confirmation', views.order_confirmed, name= 'order_confirmed'),
	url(r'^orders$', views.orders, name= 'orders'),
	path('orders/<int:year>/<int:month>/<int:day>', views.orders, name='orders'),
	path('orders/<str:update>/<int:pk>/', views.orders, name='orders'),
	path('register', views.register, name='register'),
	url(r'^supplier/', views.supplier, name= 'supplier'),
	url(r'^supplier_registration/', views.supplier_register, name= 'supplier_register'),
	path('order/<int:pk>/', views.OrderDetailView.as_view(), name='detail'),

]