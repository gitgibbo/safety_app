from django.urls import path

from . import views
from .views import lmra

app_name = 'LMRA'
urlpatterns = [
    #create LMRA
    path('create/', views.create_LMRA, name='create'),
    #home page
    path('', views.homepage, name='home'),
    #View LMRAs
    path('lmras/', views.lmras, name='lmras'),
    #View detail for single LMRA
    path('lmra/<int:pk>/', lmra.as_view(), name='lmra'),

]