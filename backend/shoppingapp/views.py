from tarfile import data_filter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Users  # or your actual model name


# Users create and delete view funtions 

class UsersView(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        email = request.data.get('email')
        try:
            user = Users.objects.get(email=email)
            user.delete()
            return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# Role-based access view
class RoleBasedView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user.role == 'admin':
            return Response({'message': f'Welcome Admin {user.username}'})
        elif user.role == 'seller':
            return Response({'message': f'Welcome Seller {user.username}'})
        elif user.role == 'user':
            return Response({'message': f'Welcome User {user.username}'})
        else:
            return Response({'error': 'Invalid role'}, status=400)


            
class UsersUpdateView(APIView):
    def put(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response({"error", "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response({"error", "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({"message","User deleted successfully"}, status=204)
        

# Add product and delele product view functions
class ProductAdd(APIView):
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        prodect = Product.objects.all()
        serializer = ProductSerializer(prodect, many=True)
        return Response(serializer.data)

class UpdateProduct(APIView):
    def put(self, request, pk):
        try:
            product = Product.object.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error", "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializers = ProductSerializer(product, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response( serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
                return Response({"error", "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message","Product deleted successfully"}, status=204)


class CategoryAdd(APIView):
    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)



        


