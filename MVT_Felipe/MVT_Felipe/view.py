from django.http import HttpResponse
from django.template import loader
import datetime




def familia(self):
    #creamos variables para un diccionario
   nombre =" Felipe"
   apellido="Bastidas"
   fecha = datetime.datetime.now()
   lista_de_notas=[2,2,3,7,2,5]
   #creamos diccionario
   diccionario = {'nombre':nombre,'apellido':apellido,'fecha':fecha,'notas':lista_de_notas}
   #cargamos la plantilla
   plantilla = loader.get_template('template.html')
   documento = plantilla.render(diccionario)
   return HttpResponse(documento)