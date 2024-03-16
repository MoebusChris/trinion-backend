from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cores.general.permissions import IsObjectCreator

from ..models import Card
from ..serializers.card import CardReadSerializer, CardWriteSerializer


class CardViewSet(viewsets.ModelViewSet):
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = [IsAuthenticated, IsObjectCreator]
    queryset = Card.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        card = serializer.save()
        read_serializer = CardReadSerializer(card, context={'request': request})

        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action in ['create', 'Partial_update', 'update']:
            return CardWriteSerializer
        
        return CardReadSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, context={'request': request}, partial=partial)
        serializer.is_valid(raise_exception=True)
        card = serializer.save()
        read_serializer = CardReadSerializer(card, context={'request': request})

        return Response(read_serializer)
    