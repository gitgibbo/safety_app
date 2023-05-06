from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'unsafe_condition'
urlpatterns = [
    path('create/', views.report_unsafe_condition, name='create'),
    path('success/', views.unsafe_condition_success, name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)