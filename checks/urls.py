from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.checks_list, name="checks_list"),
    path('list', views.checks_list, name="checks_list"),
    path('check_details/<int:pk>/', views.check_details, name="check_details"),
    path('check/new/', views.check_new, name='check_new'),
    path('check/<int:pk>/edit/', views.check_edit, name="check_edit"),

    path('direct_file', views.direct_file, name="direct_file")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)