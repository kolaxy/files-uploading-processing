from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from files.serializers import FileSerializer
from files.models import File
# Create your views here.

class FileCreateAPIView(ListCreateAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.all()

    def perform_create(self, serializer):
        serializer.save()