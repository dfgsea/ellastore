from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from bookstore.models.FoodchainStore import FoodchainStore
from bookstore.serializer.foodchainstoreserializer import FoodchainStoreSerializer

__all__= ['FoodchainStoreGet']

#GET Non Serializer
class FoodchainStoreGet(APIView):
   permission_classes=(AllowAny,)

   def get(self,request):
        id=request.GET.get('id')
        if id==None:
            query = FoodchainStore.objects.all().values(
                'id',
                'full_name', 
                'address',
                'food_chain',
                'type_of_food',
                'is_available'
                'price',
                'order_date',
                )
            return Response(query)
        else:
            query = FoodchainStore.objects.all().values(
                 'id',
                'full_name', 
                'address',
                'food_chain',
                'type_of_food',
                'is_available'
                'price',
                'order_date',
                ).filter(id=id)
            return Response(query)


#GET Serializer
   def get(self,request):
        query=FoodchainStore.objects.all()
        serializer=FoodchainStoreSerializer(query, many=True)
        return Response(serializer.data)

#POST        
   def post(self,request):
        print(request.data)
        serializer = FoodchainStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# #PUT
   def put(self,request):
       id=request.GET.get('id')
       foodchain_object = FoodchainStore.objects.get(id=id) 
       data = request.data

       foodchain_object.full_name = data["full_name"]
       foodchain_object.address = data["address"]
       foodchain_object.food_chain = data["food_chain"]
       foodchain_object.type_of_food = data["type_of_food"]
       foodchain_object.is_available = data["is_available"]
       foodchain_object.price = data["price"]
       foodchain_object.order_date = data["order_date"]       

       foodchain_object.save()                            

       serializer = FoodchainStoreSerializer(foodchain_object)
       return Response(serializer.data)