from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bookstore.models.GuitarStore import GuitarStore
from bookstore.serializer.guitarstoreserializer import GuitarStoreSerializer

__all__= ['GuitarStoreGet']

#GET Non Serializer
class GuitarStoreGet(APIView):
   permission_classes=(AllowAny,)

   def get(self,request):
        id=request.GET.get('id')
        if id==None:
            query = GuitarStore.objects.all().values(
                'id',
                'full_name', 
                'guitar_type',
                'brand_name',
                'is_available',
                'price',
                'color',
                'order_date',
                )
            return Response(query)
        else:
            query = GuitarStore.objects.all().values(
                'id',
                'full_name', 
                'guitar_type',
                'brand_name',
                'is_available',
                'price',
                'color',
                'order_date',
                ).filter(id=id)
            return Response(query)


#GET Serializer
   def get(self,request):
        query=GuitarStore.objects.all()
        serializer=GuitarStoreSerializer(query, many=True)
        return Response(serializer.data)

#POST        
   def post(self,request):
        print(request.data)
        serializer = GuitarStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# #PUT
   def put(self,request):
       id=request.GET.get('id')
       guitar_object = GuitarStore.objects.get(id=id) 
       data = request.data

       guitar_object.full_name = data["full_name"]
       guitar_object.guitar_type = data["guitar_type"]
       guitar_object.brand_name = data["brand_name"]
       guitar_object.is_available = data["is_available"]
       guitar_object.price = data["price"]
       guitar_object.color = data["color"]
       guitar_object.order_date = data["order_date"]       

       guitar_object.save()                            

       serializer = GuitarStoreSerializer(guitar_object)
       return Response(serializer.data)