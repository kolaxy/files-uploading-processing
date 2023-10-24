from django.urls import path, re_path
from files.views import FileCreateAPIView, FileListAPIView
urlpatterns = [
    path('upload/', FileCreateAPIView.as_view(), name='upload'),
    path('files/', FileListAPIView.as_view(), name='list'),
]