from rest_framework import serializers
from files.models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'

    uploaded_at = serializers.DateTimeField(read_only=True)
    processed = serializers.BooleanField(read_only=True)