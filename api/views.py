
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


# แสดงสินค้าทั้งหมด และเพิ่มสินค้าใหม่
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# ดู แก้ไข และลบสินค้าแต่ละรายการ
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
