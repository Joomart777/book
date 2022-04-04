from django.shortcuts import render

# Create your views here.

from rest_framework.generics import *

from book_app.models import *
from book_app.serializers import ProductSerializer


class ListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = ProductSerializer

class DeleteUpdateRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = ProductSerializer
