from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view  # for django api to have https methods.
from rest_framework.response import Response # to have full response method.



# Create your views here.
@api_view()
def product_list(request):
    return Response ("ok")
    