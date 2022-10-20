from . import views # '.' means current file(dir)
from django.urls import path 


urlpatterns = [        
    path('', views.translator_view, name = 'translator_view')
]