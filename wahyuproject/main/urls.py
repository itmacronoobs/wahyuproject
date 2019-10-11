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
	url(r'^orders$', views.orders, name= 'orders'),
	path('register', views.register, name='register'),
	url(r'^supplier/', views.supplier, name= 'supplier'),
	path('order/<int:pk>/', views.OrderDetailView.as_view(), name='detail'),

]