from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from files.serializers import FileSerializer
from files.models import File

class FileCreateAPIView(APIView):
    serializer_class = FileSerializer

    def post(self, request, format=None) -> Response:
        """
        File upload
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListAPIView(ListAPIView):
    serializer_class = FileSerializer

    def get_queryset(self) -> Response:
        """
        Return a list of all files include processed status
        """
        return File.objects.all()