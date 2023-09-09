from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/int:<id>/',views.product_details), # the id enables us to call for single product should be included in views after a request. int enable to change value to int.
]
