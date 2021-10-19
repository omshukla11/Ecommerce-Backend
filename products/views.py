from django.http.response import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import ( mixins, generics, status)
from products.models import Categories, Product
from products.serializers import CategorySerializer, ProductSerializer

# Create your views here.

# Function based views

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Task List':'/task/',
        'Detail View': '/task/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def CategoryList(request):
    api_urls = {
        'MoCo': "Mobiles & Computers",
        'TVAE': "TV, Appliances & Electronics",
        'MFas': "Men's Fashion",
        'WFas': "Women's Fashion",
        'Book': "Books",
        'Kitc': "Kitchen"
    }
    return Response(api_urls)

@api_view(['GET'])
def productView(request):
    instance = Product.objects.all()
    serializer = ProductSerializer(instance, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetailView(request, pk):
    instance = Product.objects.filter(id=pk)
    serializer = ProductSerializer(instance, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def productCreateView(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET', 'POST'])
def productUpdateView(request, pk):
    product = Product.objects.filter(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Class based views

# class ProductList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ProductList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class ProductDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def delete(self, request, pk, format=None):
#         product = self.get_object(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ProductDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CategoriesList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryItemsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        id = Categories.objects.filter(short=self.kwargs['pk'])
        print(id[0])
        return Product.objects.filter(category=id[0])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)