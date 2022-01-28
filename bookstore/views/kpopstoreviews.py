#from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bookstore.models.KpopStore import KpopStore
from bookstore.serializer.kpopstoreserializer import KpopStoreSerializer

__all__= ['MusicStoreGet']

#GET Non Serializer
class KpopStoreGet(APIView):
   permission_classes=(AllowAny,)

   def get(self,request):
        id=request.GET.get('id')
        if id==None:
            query = KpopStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'singer_name',
                'album_title',
                'is_available',
                'price',
                'order_date',
                )
            return Response(query)
        else:
            query = KpopStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'singer_name',
                'album_title',
                'is_available',
                'price',
                'order_date',
                ).filter(id=id)
            return Response(query)


#GET Serializer
   def get(self,request):
        query=KpopStore.objects.all()
        serializer=KpopStoreSerializer(query, many=True)
        return Response(serializer.data)

#POST        
   def post(self,request):
        print(request.data)
        serializer = KpopStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# #PUT
   def put(self,request):
       id=request.GET.get('id')
       kpop_object = KpopStore.objects.get(id=id) 
       data = request.data

       kpop_object.full_name = data["full_name"]
       kpop_object.address = data["address"]
       kpop_object.singer_name = data["singer_name"]
       kpop_object.album_title = data["album_title"]
       kpop_object.is_available = data["is_available"]
       kpop_object.price = data["price"]
       kpop_object.order_date = data["order_date"]       

       kpop_object.save()                            

       serializer = KpopStoreSerializer(kpop_object)
       return Response(serializer.data)