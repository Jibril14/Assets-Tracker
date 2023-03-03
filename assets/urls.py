from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.ListCreateCategoryAPIView.as_view(), name="create-category"),
    path('asset/company/<str:company_name>/', views.CreateAssetsAPIView.as_view(),
          name='create-assets'),
    path('asset/all/', views.ListAssetsAPIView.as_view(), name='list-assets'),
    path('asset/update/<int:pk>', views.UpdateAssetsAPIView.as_view(), name='update-assets'),
    path('asset/delete/<int:pk>', views.DeleteAssetsAPIView.as_view(), name='delet-asset'),
    path('assetlog/<int:pk>/', views.CreateAssetLogsAPIView.as_view(),
          name='create-assets-log'),
    path('assetlog/all/', views.ListAssetLogsAPIView.as_view(), name='list-assets'),
]
