from django.shortcuts import get_list_or_404, render, get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Pin, Board
from .serializers import PinSerializer, BoardSerializer


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetail(APIView):
    
    def get_object(self, pk):
        return get_object_or_404(Board, id=pk)

    def get(self, request, pk, *args, **kwargs):
        board       = self.get_object(pk)
        serializer  = BoardSerializer(board)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        board       = self.get_object(pk)
        serializer  = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, *args, **kwargs):
        board   = self.get_object(pk)
        board.delete()
        return Response(status=204)


class BoardPinList(APIView):

    def get_queryset(self, board_id):
        queryset    = get_list_or_404(Pin, board__id=board_id)
        return queryset
    
    def get(self, request, board_id, *args, **kwargs):
        pass
    
