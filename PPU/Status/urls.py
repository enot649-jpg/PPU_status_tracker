from django.urls import path
from . import views

app_name = 'Status'

urlpatterns = [
    path('main/sogl/', views.sogl, name='sogl'),
    path('main/sogl/create/', views.create_sogl, name='create_sogl'),
    path('main/sogl/export/', views.export_sogl, name='export_sogl'),
    path('main/sogl/<int:pk>/edit/', views.edit_sogl, name='edit_sogl'),
    path('main/sogl/<int:pk>/delete/', views.delete_sogl, name='sogl_delete'),
    path('main/sogl/<int:pk>/history/', views.history_sogl, name='sogl_history'),
    path('api/sogl/', views.SoglListAPIView.as_view(), name='sogl_api_view'),
]
