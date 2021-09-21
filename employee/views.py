from django.shortcuts import render

# ViewSets define the view behavior.
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
# Employee Viewset
class EmployeeViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def create(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"error": False, "message": "Success"},status.HTTP_201_CREATED)
        except:
            return Response({"error": True, "message": "Something went wrong"},status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def list(self, request):
        try:
            employee = Employee.objects.all()
            serializer = EmployeeSerializer(employee, many=True, context={"request": request})
            return Response({"error": False, "message": "Success", "data": serializer.data}, status.HTTP_200_OK)
        except:
            return Response({"error": True, "message": "Something went wrong", "data":[]},status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            employee = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(employee, context={"request": request})
            return Response({"error": False, "message": "Success", "data": serializer.data},status.HTTP_200_OK)
        except:
            return Response({"error": True, "message": "Something went wrong", "data":[]},status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            employee = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            return Response({"error": False, "message": "Success"},status.HTTP_200_OK)
        except:
            return Response({"error": True, "message": "Something went wrong"},status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            employee = get_object_or_404(queryset, pk=pk)
            employee.delete()
            return Response({"error": False, "message": "Success"},status.HTTP_200_OK)
        
        except:
            return Response({"error": True, "message": "Something went wrong"},status.HTTP_500_INTERNAL_SERVER_ERROR)
