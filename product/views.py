from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from .models import Product,Description,Category,Productclass,Brand,Topproduct,OnlyOneProduct
from .serializers import ProductSerializer,descriptionSerializers,CategorySerializer,ClassSerializers,BrandSerializers,TopproductSerializers,OnlyOneProSerializers,ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.authentication import BaseAuthentication

#Pagination import
from rest_framework.pagination import PageNumberPagination

#import filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.

class ProductListView(ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['category__name', 'category__id', 'brand__name', 'productclass__name']

    def get_queryset(self):
        """
        Foydalanuvchi so‘ragan til bo‘yicha `title` ni filtrlaydi.
        """
        queryset = super().get_queryset()
        request = self.request
        lang = request.GET.get('lang', 'en')  # Standart til English
        
        search_title = request.GET.get('search', None)
        if search_title:
            title_field = f'title_{lang}'
            filter_kwargs = {f"{title_field}__icontains": search_title}
            queryset = queryset.filter(**filter_kwargs)

        return queryset

    # def get_search_fields(self, request):
    #     search_param = request.GET.get('search', '')
    #     search_list = eval(search_param) if search_param else []
        
    #     search_fields = []
    #     for term in search_list:
    #         search_fields.extend(['title','category__id__icontains', 'category__name__icontains', 'brand__name__icontains'])
    #     return search_fields

    # def get(self, request, *args, **kwargs):
    #     self.search_fields = self.get_search_fields(request)
    #     return super().get(request, *args, **kwargs)

class SingleProductListView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 9
class ProductPagination(ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ['category__name','category__id','brand__name','productclass__name']


class CategoryListView(ListAPIView):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class ClassListApiView(ListAPIView):
    queryset = Productclass.objects.all().order_by('id')
    serializer_class = ClassSerializers

class BrandListapiview(ListAPIView):
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializers

class TopproductAPiView(ListAPIView):
    queryset = Topproduct.objects.all().order_by('-id')
    serializer_class = TopproductSerializers

class SingleCategoryListView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class OnlyProListView(ListAPIView):
    queryset = OnlyOneProduct.objects.all()
    serializer_class = OnlyOneProSerializers



