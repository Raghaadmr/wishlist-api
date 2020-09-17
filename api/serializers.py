from rest_framework import serializers
from django.contrib.auth.models import User
from items.models import Item, FavoriteItem

class RigesterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name',]

    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.set_password(new_user.password)
        new_user.save()
        return new_user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'first_name','last_name']

class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name = 'api-detail',lookup_field = 'id',lookup_url_kwarg = 'item_id')
    added_by= UserSerializer()
    favourited  = serializers.SerializerMethodField()

    class Meta:
    		model = Item
    		fields = ['image', 'name','detail', 'added_by', 'favourited']

    def get_favourited (self , obj):
        return obj.favoriteitem_set.count()

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ['user']

class ItemDetailsSerializer(serializers.ModelSerializer):
    favourited_by = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['name' , 'image', 'description' , 'favourited_by']

    def get_favourited_by(self, obj):
        return FavoriteSerializer(obj.favoriteitem_set.all(), many=True).data
