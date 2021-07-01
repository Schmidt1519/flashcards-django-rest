from .models import Collection
from .models import Card
from .serializers import CollectionSerializer
from .serializers import CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.


class CollectionList(APIView):

    def get(self, request):
        try:
            collection = Collection.objects.all()
            serializer = CollectionSerializer(collection, many=True)
            return Response(serializer.data)
        except Collection.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardList(APIView):

    def get(self, request):
        try:
            card = Card.objects.all()
            serializer = CardSerializer(card, many=True)
            return Response(serializer.data)
        except Card.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardDetail(APIView):

    def get_object(self, collection):
        try:
            return Card.objects.filter(collection=collection)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, collection):
        try:
            card = self.get_object(collection)
            serializer = CardSerializer(card, many=True)
            return Response(serializer.data)
        except Collection.DoesNotExist:
            raise Http404
