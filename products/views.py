from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Sales':'/sales/',
        'Detail View': '/sales/<int:id>/',
        'New Sale': '/new-sale/',
        'Update Sale': '/update-sale/<int:id>/'
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