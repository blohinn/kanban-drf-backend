from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Board, Column, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
        read_only_fields = ('id',)


class ColumnSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = Column
        fields = '__all__'
        read_only_fields = ('id', 'board')

    def get_cards(self, instance):
        cards = instance.cards.all().order_by('-order')
        return CardSerializer(cards, many=True).data


class BoardSerializer(serializers.ModelSerializer):
    columns = SerializerMethodField()

    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('id', 'owner')

    def get_columns(self, instance):
        columns = instance.columns.all().order_by('-order')
        return ColumnSerializer(columns, many=True).data
