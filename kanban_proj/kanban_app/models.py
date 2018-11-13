from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Column(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='columns')

    order = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255)
    color_hex = models.CharField(max_length=7, default='#000066')

    def __str__(self):
        return self.name


class Card(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='cards')

    order = models.PositiveIntegerField(default=0)
    body = models.TextField()

    def __str__(self):
        return self.body
