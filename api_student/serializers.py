from web_super_admin.models import *
from rest_framework import serializers

class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'

