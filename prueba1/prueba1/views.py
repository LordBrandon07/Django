from django.http import HttpResponse
import datetime

def saludo(request):
    documento= "<html><body><h1>viva colombia, viva falcao</h1></body></html>"
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("nospi mostro")

def fechaActual(request):
    fecha= datetime.datetime.now()
    documento= "<html><body><h2>fecha y hora actual: %s</h2></body></html>" % fecha
    return HttpResponse(documento)

def calculaEdad(request, agno, anho):
    periodo=agno-2023
    edadFutura=anho+periodo
    documento= "<html><body><h2>En el año %s tendras %s años</h2></body></html>"% (agno, edadFutura)

    return HttpResponse(documento)