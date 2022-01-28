#from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bookstore.models.SneakersStore import SneakersStore
from bookstore.serializer.sneakersstoreserializer import SneakersStoreSerializer

__all__= ['SneakersStoreGet']

#GET Non Serializer
class SneakersStoreGet(APIView):
   permission_classes=(AllowAny,)

   def get(self,request):
        id=request.GET.get('id')
        if id==None:
            query = SneakersStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'brand_name',
                'size',
                'color',
                'is_available',
                'price',
                'order_date',
                )
            return Response(query)
        else:
            query = SneakersStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'brand_name',
                'size',
                'color',
                'is_available',
                'price',
                'order_date',
                ).filter(id=id)
            return Response(query)


#GET Serializer
   def get(self,request):
        query=SneakersStore.objects.all()
        serializer=SneakersStoreSerializer(query, many=True)
        return Response(serializer.data)

#POST        
   def post(self,request):
        print(request.data)
        serializer = SneakersStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# #PUT
   def put(self,request):
       id=request.GET.get('id')
       sneakers_object = SneakersStore.objects.get(id=id) 
       data = request.data

       sneakers_object.full_name = data["full_name"]
       sneakers_object.address = data["address"]
       sneakers_object.brand_name = data["brand_name"]
       sneakers_object.size = data["size"]
       sneakers_object.color = data["color"]
       sneakers_object.is_available = data["is_available"]
       sneakers_object.price = data["price"]
       sneakers_object.order_date = data["order_date"]       

       sneakers_object.save()                            

       serializer = SneakersStoreSerializer(sneakers_object)
       return Response(serializer.data)