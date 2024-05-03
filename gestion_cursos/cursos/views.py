from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .services import *

@csrf_exempt
def crear_curso(request):
    response = crear_curso()
    return JsonResponse({'message': response})

@csrf_exempt
def crear_profesor(request):
    response = crear_profesor()
    return JsonResponse({'message': response})

@csrf_exempt
def crear_estudiante(request):
    response = crear_estudiante()
    return JsonResponse({'message': response})

@csrf_exempt
def crear_direccion(request):
    response = crear_direccion()
    return JsonResponse({'message': response})

@csrf_exempt
def obtiene_estudiante(request):
    response = obtiene_estudiante()
    return JsonResponse({'message': response})

@csrf_exempt
def obtiene_profesor(request):
    response = obtiene_profesor()
    return JsonResponse({'message': response})

@csrf_exempt
def obtiene_curso(request):
    response = obtiene_curso()
    return JsonResponse({'message': response})

@csrf_exempt
def agrega_profesor_a_curso(request):
    response = agrega_profesor_a_curso()
    return JsonResponse({'message': response})

@csrf_exempt
def agrega_cursos_a_estudiante(request):
    response = agrega_cursos_a_estudiante()
    return JsonResponse({'message': response})

@csrf_exempt
def imprime_estudiante_cursos(request):
    response = imprime_estudiante_cursos()
    return JsonResponse({'message': response})
