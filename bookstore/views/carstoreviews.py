#from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bookstore.models.CarStore import CarStore
from bookstore.serializer.carstoreserializer import CarStoreSerializer

__all__= ['CarStoreGet']

#GET Non Serializer
class CarStoreGet(APIView):
   permission_classes=(AllowAny,)

   def get(self,request):
        id=request.GET.get('id')
        if id==None:
            query = CarStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'brand_name',
                'color',
                'is_available',
                'price',
                'order_date',
                )
            return Response(query)
        else:
            query = CarStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'brand_name',
                'color',
                'is_available',
                'price',
                'order_date',
                ).filter(id=id)
            return Response(query)


#GET Serializer
   def get(self,request):
        query=CarStore.objects.all()
        serializer=CarStoreSerializer(query, many=True)
        return Response(serializer.data)

#POST        
   def post(self,request):
        print(request.data)
        serializer = CarStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# #PUT
   def put(self,request):
       id=request.GET.get('id')
       car_object = CarStore.objects.get(id=id) 
       data = request.data

       car_object.full_name = data["full_name"]
       car_object.address = data["address"]
       car_object.brand_name = data["brand_name"]
       car_object.color = data["color"]
       car_object.is_available = data["is_available"]
       car_object.price = data["price"]
       car_object.order_date = data["order_date"]       

       car_object.save()                            

       serializer = CarStoreSerializer(car_object)
       return Response(serializer.data)