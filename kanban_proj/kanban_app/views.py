from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404

from .serializers import BoardSerializer, ColumnSerializer, CardSerializer
from .models import Board, Column, Card


class BoardList(generics.ListCreateAPIView):
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.request.user.boards.all()


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_object(self):
        board = get_object_or_404(Board, pk=self.kwargs['pk'])
        if board.owner != self.request.user:
            raise PermissionDenied
        return board


class ColumnListByBoard(generics.ListCreateAPIView):
    lookup_field = 'board_id'
    serializer_class = ColumnSerializer

    def __get_board(self):
        board = get_object_or_404(Board, pk=self.kwargs['board_id'])
        if board.owner != self.request.user:
            raise PermissionDenied
        return board

    def get_queryset(self):
        return self.__get_board().columns.all().order_by('-order')

    def perform_create(self, serializer):
        serializer.save(board=self.__get_board())


class ColumnDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    def get_object(self):
        column = get_object_or_404(Column, pk=self.kwargs['pk'])
        if column.board.owner != self.request.user:
            raise PermissionDenied
        return column

    def perform_update(self, serializer):
        if serializer.validated_data['board'].owner != self.request.user:
            raise PermissionDenied


class CardListByColumn(generics.ListCreateAPIView):
    lookup_field = 'column_id'
    serializer_class = CardSerializer

    def __get_column(self):
        column = get_object_or_404(Column, pk=self.kwargs['column_id'])
        if column.board.owner != self.request.user:
            raise PermissionDenied
        return column

    def get_queryset(self):
        return self.__get_column().cards.all().order_by('-order')

    def perform_create(self, serializer):
        serializer.save(column=self.__get_column())


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_object(self):
        card = get_object_or_404(Card, pk=self.kwargs['pk'])
        if card.column.board.owner != self.request.user:
            raise PermissionDenied
        return card

    def perform_update(self, serializer):
        if serializer.validated_data['column'].board.owner != self.request.user:
            raise PermissionDenied
