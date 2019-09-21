from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name= 'index'),
	url(r'main', views.index, name= 'index'),
	url(r'excel', views.excel, name= 'excel'),
	url(r'order', views.order, name= 'order'),
]