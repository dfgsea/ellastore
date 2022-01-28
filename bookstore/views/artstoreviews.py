#from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bookstore.models.ArtStore import ArtStore
from bookstore.serializer.artstoreserializer import ArtStoreSerializer

__all__= ['ArtStoreGet']

#GET Non Serializer
class ArtStoreGet(APIView):
   permission_classes=(AllowAny,)

   def get(self,request):
        id=request.GET.get('id')
        if id==None:
            query =ArtStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'artist_name',
                'art_title',
                'is_available',
                'price',
                'order_date',
                )
            return Response(query)
        else:
            query = ArtStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'artist_name',
                'art_title',
                'is_available',
                'price',
                'order_date'
                ).filter(id=id)
            return Response(query)


#GET Serializer
   def get(self,request):
        query=ArtStore.objects.all()
        serializer=ArtStoreSerializer(query, many=True)
        return Response(serializer.data)

#POST        
   def post(self,request):
        print(request.data)
        serializer = ArtStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# #PUT
   def put(self,request):
       id=request.GET.get('id')
       art_object = ArtStore.objects.get(id=id) 
       data = request.data

       art_object.full_name = data["full_name"]
       art_object.address = data["address"]
       art_object.artist_name = data["artist_name"]
       art_object.art_title = data["album_title"]
       art_object.is_available = data["is_available"]
       art_object.price = data["price"]
       art_object.order_date = data["order_date"]       

       art_object.save()                            

       serializer = ArtStoreSerializer(art_object)
       return Response(serializer.data)