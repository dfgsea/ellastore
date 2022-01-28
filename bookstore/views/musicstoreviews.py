#from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bookstore.models.MusicStore import MusicStore
from bookstore.serializer.musicstoreserializer import MusicStoreSerializer

__all__= ['MusicStoreGet']

#GET Non Serializer
class MusicStoreGet(APIView):
   permission_classes=(AllowAny,)

   def get(self,request):
        id=request.GET.get('id')
        if id==None:
            query = MusicStore.objects.all().values(
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
            query = MusicStore.objects.all().values(
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
        query=MusicStore.objects.all()
        serializer=MusicStoreSerializer(query, many=True)
        return Response(serializer.data)

#POST        
   def post(self,request):
        print(request.data)
        serializer = MusicStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# #PUT
   def put(self,request):
       id=request.GET.get('id')
       music_object = MusicStore.objects.get(id=id) 
       data = request.data

       music_object.full_name = data["full_name"]
       music_object.address = data["address"]
       music_object.singer_name = data["singer_name"]
       music_object.album_title = data["album_title"]
       music_object.is_available = data["is_available"]
       music_object.price = data["price"]
       music_object.order_date = data["order_date"]       

       music_object.save()                            

       serializer = MusicStoreSerializer(music_object)
       return Response(serializer.data)