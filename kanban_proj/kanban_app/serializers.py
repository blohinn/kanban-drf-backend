from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Board, Column, Card


class CardSerializer(serializers.ModelSerializer):
    column = serializers.PrimaryKeyRelatedField(queryset=Column.objects.all(), style={
        'base_template': 'input.html'
    })

    class Meta:
        model = Card
        fields = '__all__'
        read_only_fields = ('id',)


class ColumnSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Column
        fields = '__all__'
        read_only_fields = ('id', 'board')

    def get_cards(self, instance):
        cards = instance.cards.all().order_by('-order')
        return CardSerializer(cards, many=True).data


class BoardSerializer(serializers.ModelSerializer):
    columns = SerializerMethodField(read_only=True)

    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('id', 'owner')

    def get_columns(self, instance):
        columns = instance.columns.all().order_by('id')
        return ColumnSerializer(columns, many=True).data
