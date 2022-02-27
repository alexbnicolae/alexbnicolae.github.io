from feed.models import ContactBook
from rest_framework import serializers


class ContactBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactBook
        fields = "__all__"