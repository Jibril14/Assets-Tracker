from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.ListCreateCompanyAPIView.as_view(), name="create-company"),
    path('company/update/<int:pk>/', views.RetrieveUpdateCompanyAPIView.as_view(), name="update-company"),
]
