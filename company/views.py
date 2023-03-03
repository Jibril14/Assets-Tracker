from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from company.models import Company
from company.serializers import CompanySerializer


class ListCreateCompanyAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    

class RetrieveUpdateCompanyAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer

    def  get_queryset(self):
        company = Company.objects.get(pk=self.kwargs["pk"]) # get a single instance
        return Company.objects.filter(company_name=company)
    