from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

# Create your views here.
class SumaView(APIView): #APIView para establecer que es una api
    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        suma=int(num_uno)+ int(num_dos)
        return Response(suma, status=status.HTTP_200_OK)
class RestaView(APIView):
    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        resta=int(num_uno)-int(num_dos)
        return Response(resta, status=status.HTTP_200_OK)
class MultiplicacionView(APIView):
    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        multiplicacion=int(num_uno)*int(num_dos)
        return Response(multiplicacion, status=status.HTTP_200_OK)
class DivisionView(APIView):
    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        if num_dos!=0:
            division=int(num_uno)/int(num_dos)
            return Response(division, status=status.HTTP_200_OK)
        elif num_dos==0:
            dividir='no se puede dividir por 0 unu'
            return Response(dividir, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
