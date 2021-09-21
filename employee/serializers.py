# Serializers define the API representation.
from rest_framework import serializers

from .models import Employee, Attendance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        
class EmployeeAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ["employee_id", "status"]
