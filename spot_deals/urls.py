from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home_page'),
    path('assets/<int:asset_id>/', assets),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive),
]
