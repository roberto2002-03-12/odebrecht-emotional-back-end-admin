from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view

from .models import professional
from .serializers import professionalSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def professional_list(request):
    if request.method == 'GET':
        data = professional.objects.all()

        serializer = professionalSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = professionalSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def professional_detail(request, pk):
    try:
        Professionals = professional.objects.get(pk=pk)
    except professional.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = professionalSerializer(Professionals)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = professionalSerializer(Professionals, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Professionals.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
class ProfessionalView(APIView):
    
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        professionals = professional.objects.all()
        serializer = professionalSerializer(professionals, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = professionalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''