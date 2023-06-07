from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('load&<slug:my_string>', LoadVideo.as_view(), name='load'),
]