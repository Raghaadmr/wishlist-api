from django.shortcuts import render
from rest_framework import filters
from .serializers import RigesterSerializer, ItemListSerializer, ItemDetailsSerializer, UserSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .permissions import OnlyAddedByUser
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
from items.models import Item

class Rigester(CreateAPIView):
    serializer_class = RigesterSerializer


class ItemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name','description',]
    ordering_fields = '__all__'


class ItemDetails(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [OnlyAddedByUser, IsAuthenticated]
