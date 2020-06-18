from django.urls import path
from . import views
# from rest_framework import routers


urlpatterns = [
    path('', views.AllMarks.as_view({'get': 'list', 'post':'create'})),
    # path('', views.AllMarks.as_view(), name='allmarks')
]
