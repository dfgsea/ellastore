#from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bookstore.models.BagStore import BagStore
from bookstore.serializer.bagstoreserializer import BagStoreSerializer

__all__= ['BagStoreGet']

#GET Non Serializer
class BagStoreGet(APIView):
   permission_classes=(AllowAny,)

   def get(self,request):
        id=request.GET.get('id')
        if id==None:
            query = BagStore.objects.all().values(
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
            query = BagStore.objects.all().values(
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
        query=BagStore.objects.all()
        serializer=BagStoreSerializer(query, many=True)
        return Response(serializer.data)

#POST        
   def post(self,request):
        print(request.data)
        serializer = BagStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# #PUT
   def put(self,request):
       id=request.GET.get('id')
       bag_object = BagStore.objects.get(id=id) 
       data = request.data

       bag_object.full_name = data["full_name"]
       bag_object.address = data["address"]
       bag_object.brand_name = data["brand_name"]
       bag_object.color = data["color"]
       bag_object.is_available = data["is_available"]
       bag_object.price = data["price"]
       bag_object.order_date = data["order_date"]       

       bag_object.save()                            

       serializer = BagStoreSerializer(bag_object)
       return Response(serializer.data)