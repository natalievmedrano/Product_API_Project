from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import status

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many= True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer= ProductSerializer(data= request.data)
        if serializer.is_valid() == True:
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
   

@api_view(['GET','PUT'])
def product_detail(request,pk):
  
    product= get_object_or_404(Product , pk=pk)
    if request.method == 'GET': 
     serializer = ProductSerializer(product)
     return Response(serializer.data)
    elif request.method == 'PUT':
     serializer = ProductSerializer(product, data=request.data)
     serializer.is_valid(raise_exception=True)
     serializer.save()
     return Response(serializer.data)

    




