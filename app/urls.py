from django.urls import path
from . import views

urlpatterns = [
    path('run-calculations/', views.run_calculations, name='run_calculations'),
]
