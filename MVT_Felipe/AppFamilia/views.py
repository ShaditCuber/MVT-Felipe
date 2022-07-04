from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from AppFamilia.models import Familia





def familia(self):
    #creamos variables para un diccionario
   familia1 =  Familia(nombre='Felipe', apellido='Bastidas', fecha_nacimiento=datetime.date(1999,1,1), edad=22, licenciaConducirActivada=False)
   familia2 =  Familia(nombre='Juan', apellido='Perez', fecha_nacimiento=datetime.date(1990,1,12), edad=31, licenciaConducirActivada=True)
   familia3 =  Familia(nombre='Maria', apellido='Gonzalez', fecha_nacimiento=datetime.date(1980,1,1), edad=40, licenciaConducirActivada=False)
   familia1.save()
   familia2.save()
   familia3.save()  
   listaFamilia=[familia1,familia2,familia3]
   
   #creamos diccionario
   diccionario = {'lista':listaFamilia}
   #cargamos la plantilla
   plantilla = loader.get_template('template.html')
   documento = plantilla.render(diccionario)
   return HttpResponse(documento)