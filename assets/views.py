from django.shortcuts import render
from .models import Assets, AssetLogs, Category
from company.models import Company
from .serializers import AssetsSerializer, AssetLogSerializer, CategorySerializer
from rest_framework import generics, exceptions, permissions, status
from rest_framework.response import Response

# Asset Category
class ListCreateCategoryAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# Asset 
class CreateAssetsAPIView(generics.CreateAPIView):
    serializer_class = AssetsSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        try:
            company = Company.objects.get(company_name=self.kwargs["company_name"])
        except BaseException:
            raise exceptions.APIException("Company not found!")
        return Company.objects.filter(company_name=company.company_name)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            serializer.save(          
                company = Company.objects.get(company_name=self.kwargs["company_name"]))
            

class ListAssetsAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AssetsSerializer
    queryset = Assets.objects.all()


class UpdateAssetsAPIView(generics.UpdateAPIView):
   serializer_class = AssetsSerializer
   permission_classes = [permissions.IsAdminUser]

   def  get_queryset(self):
      asset_id = Assets.objects.get(id=self.kwargs["pk"])
      return Assets.objects.filter(id=asset_id.id)


class DeleteAssetsAPIView(generics.RetrieveDestroyAPIView):
   serializer_class =AssetsSerializer
   permissions_classes = [permissions.IsAdminUser]
     
   def get_queryset(self):  
       asset_id = Assets.objects.get(id=self.kwargs["pk"])
       return Assets.objects.filter(id=asset_id.id)
   
   def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response( {"success": "Deleted Succesfully"}, status=status.HTTP_204_NO_CONTENT)
       


# Asset Log
class CreateAssetLogsAPIView(generics.CreateAPIView):
    serializer_class = AssetLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            asset = Assets.objects.get(id=self.kwargs["pk"])
        except BaseException:
            raise exceptions.APIException("Asset not found!")
        return Assets.objects.filter(id=asset.id)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            user = self.request.user
            serializer.save(
                collected_by = user,      
                asset = Assets.objects.get(id=self.kwargs["pk"]))
        

class ListAssetLogsAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AssetLogSerializer
    queryset = AssetLogs.objects.all()



