from rest_framework import serializers


class GedIdDealSerializer(serializers.Serializer):
    idDeal = serializers.IntegerField()