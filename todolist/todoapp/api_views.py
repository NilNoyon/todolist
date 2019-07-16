from http import client
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . serializers import *
# Create your views here.

class Lists(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request,format=None):
        snippet = self.get_object(pk)
        serializer = ListSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ListSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
