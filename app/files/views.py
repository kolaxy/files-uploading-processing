from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from files.serializers import FileSerializer
from files.models import File
from files.tasks import file_processing

import logging
logger = logging.getLogger(__name__)

class FileCreateAPIView(APIView):
    serializer_class = FileSerializer

    def post(self, request, format=None) -> Response:
        """
        File upload
        """
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            if serializer.is_valid():
                file = serializer.save()
                transaction.on_commit(lambda: file_processing.delay(file.pk))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.error(f"Invalid request data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("An error occurred during file uploading")
            return Response({"detail": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FileListAPIView(ListAPIView):
    serializer_class = FileSerializer


    def get_queryset(self) -> Response:
        """
        Return a list of all files include processed status
        """
        return File.objects.all()