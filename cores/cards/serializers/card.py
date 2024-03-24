from rest_framework import serializers

from cores.users.serializers.user import UserReadSerializer, UserWriteSerializer  # type: ignore # noqa: I100, F401

from ..models.card import Card


class CardReadSerializer(serializers.ModelSerializer):
    creator = UserReadSerializer()

    class Meta:
        model = Card
        fields = '__all__'


class CardWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
        read_only_fields = ('creator',)

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        pass
