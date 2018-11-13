from django.urls import path

from .views import BoardList, BoardDetail, ColumnListByBoard, ColumnDetail, CardListByColumn, CardDetail, \
    ReorderColumnCards

app_name = 'kanban_app'
urlpatterns = [
    path('board/', BoardList.as_view(), name='board_list'),
    path('board/<int:pk>', BoardDetail.as_view(), name='board_detail'),

    path('column/board/<int:board_id>', ColumnListByBoard.as_view(), name='column_list_by_board'),
    path('column/<int:pk>/order', ReorderColumnCards.as_view(), name='order_column_cards'),
    path('column/<int:pk>', ColumnDetail.as_view(), name='column_detail'),

    path('card/column/<int:column_id>', CardListByColumn.as_view(), name='card_list_by_column'),
    path('card/<int:pk>', CardDetail.as_view(), name='card_detail')
]
