import os
from django.test import TestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch
from rest_framework.test import APIClient
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from .tasks import file_processing


def delete_test_file(filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        os.remove(file_path)


class FileModelTest(TestCase):
    def test_file_creation(self):
        # Create a File instance
        file = File.objects.create(
            file="test_file.txt",
            processed=True,
        )

        saved_file = File.objects.get(pk=file.pk)

        self.assertEqual(saved_file.file, "test_file.txt")
        self.assertEqual(saved_file.processed, True)

        delete_test_file("test_file.txt")

    def test_default_processed_value(self):
        file = File.objects.create(file="test_file.txt")

        saved_file = File.objects.get(pk=file.pk)

        self.assertEqual(saved_file.processed, False)

        delete_test_file("test_file.txt")


class FileSerializerTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_file(self):
        # Simulate a POST request with a file upload
        file_data = {
            'file': SimpleUploadedFile("test_file.txt", b"file_content"),
        }
        response = self.client.post('/upload/', file_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(File.objects.filter(file='test_file.txt').exists())

        delete_test_file("test_file.txt")

    def test_validate_file_field(self):
        # Simulate a POST request without a file
        invalid_data = {}
        response = self.client.post('/upload/', invalid_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('file', response.data)

    def test_serializer_with_get_request(self):
        # Simulate a GET request
        file1 = SimpleUploadedFile("test_file1.txt", b"file_content")
        File.objects.create(file=file1)

        file2 = SimpleUploadedFile("test_file2.txt", b"file_content")
        File.objects.create(file=file2)

        response = self.client.get('/files/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        delete_test_file("test_file1.txt")
        delete_test_file("test_file2.txt")


class FileProcessingTestCase(TestCase):

    @patch('files.tasks.logger.error')
    def test_file_processing_success(self, mock_logger_error):

        file = File.objects.create(processed=False)

        file_processing(file.id)

        file.refresh_from_db()

        self.assertTrue(file.processed)
        self.assertFalse(mock_logger_error.called)

    @patch('files.tasks.logger.error')
    def test_file_processing_failure(self, mock_logger_error):
        file = File.objects.create(processed=False)
        with patch('files.tasks.File.objects.get') as mock_file_get:
            mock_file_get.side_effect = Exception("Something went wrong")

            file_processing(file.id)

        file.refresh_from_db()

        self.assertFalse(file.processed)
        self.assertTrue(mock_logger_error.called)


class FileDetailApiViewTest(TestCase):
    def setUp(self):
        # Create test files
        f1 = SimpleUploadedFile("test_file1.txt", b"file_content")
        self.file1 = File.objects.create(file=f1)

        f2 = SimpleUploadedFile("test_file2.txt", b"file_content")
        self.file2 = File.objects.create(file=f2)

    def test_get_existing_file(self):
        # Try to get existing file (2 times)
        client = APIClient()
        response1 = client.get(f'/files/{self.file1.pk}/')
        response2 = client.get(f'/files/{self.file2.pk}/')

        expected_data1 = FileSerializer(self.file1).data
        expected_data2 = FileSerializer(self.file2).data

        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response1.data, expected_data1)

        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.data, expected_data2)

        delete_test_file("test_file1.txt")
        delete_test_file("test_file2.txt")

    def test_get_non_existing_file(self):
        # Try ro get non existing file (2 times)
        client = APIClient()

        not_real_pk1 = 1337
        not_real_pk2 = 3771

        response1 = client.get(f'/files/{not_real_pk1}/')
        response2 = client.get(f'/files/{not_real_pk2}/')

        self.assertEqual(response1.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response1.data, {"Error": "File not found."})

        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response2.data, {"Error": "File not found."})

        delete_test_file("test_file1.txt")
        delete_test_file("test_file2.txt")
