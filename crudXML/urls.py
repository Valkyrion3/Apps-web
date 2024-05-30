from django.urls import path
from . import views

urlpatterns = [
    path('', views.xmlfile_list, name='xmlfile_list'),
    path('create/', views.xmlfile_create, name='xmlfile_create'),
    path('upload/', views.xmlfile_upload, name='xmlfile_upload'),
    path('<int:pk>/', views.xmlfile_detail, name='xmlfile_detail'),
    path('<int:pk>/edit/', views.xmlfile_edit, name='xmlfile_edit'),
    path('<int:pk>/download/', views.xmlfile_download, name='xmlfile_download'),
    path('<int:pk>/delete/', views.xmlfile_delete, name='xmlfile_delete'),
]
