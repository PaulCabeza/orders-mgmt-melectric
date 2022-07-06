from rest_framework import serializers

class PoSerializer(serializers.Serializer):
    po_number = serializers.IntegerField()
