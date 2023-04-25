from django.urls import path, include
from .views import testIshla, javop

urlpatterns = [
    path('', testIshla, name='testIshla'),
    path('javop', javop, name='javop')
]