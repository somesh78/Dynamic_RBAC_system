from rest_framework import serializers
from .models import Feature, RoleFeature

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class RoleFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleFeature
        fields = '__all__'
        