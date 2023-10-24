from rest_framework import serializers
from files.models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FileSerializer, self).__init__(*args, **kwargs)

        if self.context['request'].method == 'POST':
            self.fields = {'file': self.fields['file']}