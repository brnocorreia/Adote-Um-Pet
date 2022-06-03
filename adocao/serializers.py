from rest_framework import serializers

from .models import Adocao


class AdocaoSerializer(serializers.models):
    class Meta:
        model = Adocao
        fields = ('id', 'email', 'valor', 'pet')
