from django.urls import path
from files.views import FileCreateAPIView, FileListAPIView, FileDetailApiView
urlpatterns = [
    path('upload/', FileCreateAPIView.as_view(), name='upload'),
    path('files/', FileListAPIView.as_view(), name='list'),
    path('files/<int:pk>/', FileDetailApiView.as_view(), name='file-detail'),
]
