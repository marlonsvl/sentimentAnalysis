# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.core.files import File

import urllib2
import csv
import re

import json

def eliminarMenciones(cadena):
    bandera = True
    while(bandera):
        posicion = cadena.find("@")
        if posicion!=-1:
            cad = cadena[posicion]+cadena[posicion+1]
            may = cadena[posicion+1]
            may = may.capitalize()

            cadena = cadena.replace(cad,may)
        else:
            bandera=False
    cadena = cadena.replace("#", "")
    #print cadena
    return cadena


def index(request):
    res = HttpResponse(content_type='text/csv')
    res['Content-Disposition'] = 'attachment; filename=listado.csv'
    writer = csv.writer(res)
    writer.writerow(['id','Tweets','Usuario','Numero Favoritos','Numero Retweets','Nombre'])

    if request.POST and request.FILES:
        #http://www.thuydienthacba.com/questions/4576059/getting-type-error-while-opening-an-uploaded-csv-file
        csvfile = request.FILES['csv_file'].open()  # http://stackoverflow.com/questions/10617286/getting-type-error-while-opening-an-uploaded-csv-file
        #portfolio = csv.DictReader(paramFile)
        portfolio = csv.DictReader(request.FILES['csv_file'].file)
        for i in portfolio:
            twett = ""
            twett= twett.join(i['text'])
            usuario = ""
            usuario= usuario.join(i['usuario'])
            datosjson = ""
            datosjson= datosjson.join(i['datosjson'])
            datosjson = json.loads(datosjson)

            nombre = datosjson['user']
            #nombre = json.loads(nombre)

            print type(nombre)
            # Si RT o via @ o # esta al principio se elimina el twett
            if "RT" in twett[0:3] or "via @" in twett or twett[0]=="#":
                pass
            else:
                # Si el twett tiene http y el campo de la base de datos url es diferente de vacio
                if "http" in twett and i['urls']!="":
                    response = urllib2.urlopen(i['urls'])
                    html = response.read()
                    # Si se encuentra una coincidencia del twett con el contenido de la url
                    if twett[3:20] in html:
                        pass
                    else:
                        # Se impimer el twett
                        writer.writerow([datosjson['id'],eliminarMenciones(twett),usuario, datosjson['favorite_count'], datosjson['retweet_count'], nombre['name']])
                        #eliminarMenciones(twett)
                # Si hay una url en el twett pero no en la base de datos
                elif "http" in twett:
                    # Buscamos la url en el twett
                    try:
                        url = re.search("(?P<url>https?://[^\s]+)", twett).group("url")

                        # Si se encuentra ' en una url la elimina
                        if "'" in url:
                            url = url.replace("'","")

                        response = urllib2.urlopen(url)
                        html = response.read()
                        if twett[3:20] in html:
                            pass
                        else:
                            #eliminarMenciones(twett)
                            writer.writerow([datosjson['id'],eliminarMenciones(twett),usuario, datosjson['favorite_count'], datosjson['retweet_count'], nombre['name']])
                    # Si no se encuentra la url en el twett
                    except Exception:
                        #eliminarMenciones(twett)
                        writer.writerow([datosjson['id'],eliminarMenciones(twett),usuario, datosjson['favorite_count'], datosjson['retweet_count'], nombre['name']])

                else:
                    # Se imprimer el twett
                    #eliminarMenciones(twett)
                    writer.writerow([datosjson['id'],eliminarMenciones(twett),usuario, datosjson['favorite_count'], datosjson['retweet_count'], nombre['name']])
        return res

    return render(request, "index.html", locals())