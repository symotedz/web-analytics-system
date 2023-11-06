from datetime import datetime

from web_super_admin.models import *
from rest_framework import serializers

class LibraryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryCategory
        fields = "__all__"

class LibraryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryItem
        fields = "__all__"

class LibraryReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryReservation
        fields = "__all__"

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryReservation
        fields = "__all__"

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryReservation
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"