from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('<int:id>/', views.chai_details, name='chai_details'),
    path('order/<int:id>/', views.order_chai, name='order_chai'),
    path('chai_stores/',views.chai_store_views, name='chai_stores')
]
