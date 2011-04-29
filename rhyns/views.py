from rhyns.models import DBSession
from rhyns.models import MyModel
from pyramid.response import Response

def home(request):
    return Response("Waiting for Abel template :)")

def status(request):
    return Response("Status of thunder {0}".format(request.matchdict["thunder_num"]))

def install(request):
    return Response("Installing hypervisor {0} on thunder {1}...".format(request.matchdict["hypervisor"], request.matchdict["thunder_num"]))

def poweron(request):
    return Response("Poweron thunder {0}".format(request.matchdict["thunder_num"]))

def poweroff(request):
    return Response("Poweroff thunder{0}".format(request.matchdict["thunder_num"]))

def reboot(request):
    return Response("Rebooting thunder {0}".format(request.matchdict["thunder_num"]))
