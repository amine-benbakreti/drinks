from .serializers import DrinkSerializer
from .models import Drink
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

class DrinkList(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class Drinkdetail(generics.RetrieveUpdateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class Drinkcreate(generics.CreateAPIView):
    queryset=Drink.objects.all()
    serializer_class = DrinkSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        name=serializer.validated_data.get('name')
        des=serializer.validated_data.get('description') 
        ra=serializer.validated_data.get('rate') or None
        if ra== None:
            ra = 'amine'
        serializer.save(rate=ra)


# @api_view(['GET', 'POST'])
# def drink_list(request):
#     if request.method == 'GET':
#         drinks = Drink.objects.all()
#         serializer = DrinkSerializer(drinks, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = DrinkSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def drinkdetail(request,id):
#    try:
#      drink=Drink.objects.get(pk=id)
#    except Drink.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
   
#    if request.method == 'GET':
#        serializer = DrinkSerializer(drink)
#        return Response(serializer.data) 
#    if request.method == 'PUT':
#        serializer = DrinkSerializer(drink,data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data,status=status.HTTP_200_OK)
#        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#    if request.method == 'DELETE':        
#        drink.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
    
