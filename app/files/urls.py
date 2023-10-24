from django.urls import path, re_path
from files.views import FileCreateAPIView
urlpatterns = [
    path('files/', FileCreateAPIView.as_view()),
]