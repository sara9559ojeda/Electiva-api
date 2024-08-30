from django.urls import path
from .views import SumaView
from .views import RestaView
from .views import MultiplicacionView
from .views import DivisionView


#se llama a la clase sumar
urlpatterns=[
    path('sumar',  SumaView.as_view()),
    path('restar', RestaView.as_view()),
    path('multiplicacion', MultiplicacionView.as_view()),
    path('division', DivisionView.as_view())
]