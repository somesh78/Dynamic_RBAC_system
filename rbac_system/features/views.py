from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Feature, RoleFeature
from .serializers import FeatureSerializer, RoleFeatureSerializer

class FeatureViewSet(ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class RoleFeatureViewSet(ModelViewSet):
    queryset = RoleFeature.objects.all()
    serializer_class = RoleFeatureSerializer