#from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bookstore.models.BookStore import BookStore
from bookstore.serializer.bookstoreserializer import BookStoreSerializer

__all__= ['BookStoreGet']

#GET Non Serializer
class BookStoreGet(APIView):
   permission_classes=(AllowAny,)

   def get(self,request):
        id=request.GET.get('id')
        if id==None:
            query = BookStore.objects.all().values(
                'id',
                'full_name', 
                'author',
                'book_name',
                'is_available',
                'price',
                'order_date',
                )
            return Response(query)
        else:
            query = BookStore.objects.all().values(
                'id',
                'full_name', 
                'author',
                'book_name',
                'is_available',
                'price',
                'order_date',
                ).filter(id=id)
            return Response(query)


#GET Serializer
   def get(self,request):
        query=BookStore.objects.all()
        serializer=BookStoreSerializer(query, many=True)
        return Response(serializer.data)

#POST        
   def post(self,request):
        print(request.data)
        serializer = BookStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# #PUT
   def put(self,request):
       id=request.GET.get('id')
       book_object = BookStore.objects.get(id=id) 
       data = request.data

       book_object.full_name = data["full_name"]
       book_object.author = data["author"]
       book_object.book_name = data["book_name"]
       book_object.is_available = data["is_available"]
       book_object.price = data["price"]
       book_object.order_date = data["order_date"]       

       book_object.save()                            

       serializer = BookStoreSerializer(book_object)
       return Response(serializer.data)