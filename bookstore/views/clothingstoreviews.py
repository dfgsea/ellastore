#from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bookstore.models.ClothingStore import ClothingStore
from bookstore.serializer.clothingstoreserializer import ClothingStoreSerializer

__all__= ['BookStoreGet']

#GET Non Serializer
class ClothingStoreGet(APIView):
   permission_classes=(AllowAny,)

   def get(self,request):
        id=request.GET.get('id')
        if id==None:
            query = ClothingStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'brand_name',
                'type_of_clothes',
                'is_available',
                'price',
                'order_date',
                )
            return Response(query)
        else:
            query = ClothingStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'brand_name',
                'type_of_clothes',
                'is_available',
                'price',
                'order_date',
                ).filter(id=id)
            return Response(query)


#GET Serializer
   def get(self,request):
        query=ClothingStore.objects.all()
        serializer=ClothingStoreSerializer(query, many=True)
        return Response(serializer.data)

#POST        
   def post(self,request):
        print(request.data)
        serializer = ClothingStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# #PUT
   def put(self,request):
       id=request.GET.get('id')
       clothing_object = ClothingStore.objects.get(id=id) 
       data = request.data

       clothing_object.full_name = data["full_name"]
       clothing_object.address = data["address"]
       clothing_object.brand_name = data["brand_name"]
       clothing_object.type_of_clothes = data["type_of_clothes"]
       clothing_object.is_available = data["is_available"]
       clothing_object.price = data["price"]
       clothing_object.order_date = data["order_date"]       

       clothing_object.save()                            

       serializer = ClothingStoreSerializer(clothing_object)
       return Response(serializer.data)