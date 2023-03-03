from rest_framework import serializers
from .models import Assets, AssetLogs, Category



class AssetsSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Assets
        fields = "__all__"

    def get_category(self, obj):
        return obj.category.category_name


class AssetLogSerializer(serializers.ModelSerializer):
    collected_by = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = AssetLogs
        fields = "__all__"

    def get_collected_by(self, obj):
        return obj.collected_by.username


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

