
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mainp, name='home'),
    path('chart/', views.ChartData.as_view()),
    path('custform/', views.custform, name='cdform'), 
    path('ordersform/', views.ordersform, name='ordform'),
    path('expensesform', views.expensesform, name='expform'),
    path('expensesupdateform/<expns_id>/', views.expenses_update, name='expnsupdate'),
    path('orders/', views.orders, name='ordrs'),
    path('expenses/', views.expenses, name='expns'),
    path('purchaseform/', views.poform, name='poform'),
    path('paymentsform/', views.payform, name='payform'),
    path('allprojects/', views.allpro, name='allproj'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
