import transaction

from rhyns.models import DBSession
from rhyns.models import Thunder
from rhyns.thunders_control import *
from pyramid.response import Response
from pyramid.view import view_config

# @view_config(route_name='home', renderer='template.pt')
@view_config(renderer='list.mako')
def home(request):
    session = DBSession()
    thunder = session.query(Thunder).filter(Thunder.id == "1").one()
    thunders = session.query(Thunder).all()

    for t in thunders:

        t.hypervisor = do_check_hypervisor(t)
        session.add(t)
    session.flush()
    transaction.commit()

    thunder = session.query(Thunder).filter(Thunder.id == "1").one()
    thunders = session.query(Thunder).all()

    return  {'project':thunder.status, 'thunders':thunders} # Response("Waiting for Abel template :)")



def status(request):
    session = DBSession()
    thunder = session.query(Thunder).filter(Thunder.id == request.matchdict["thunder_id"]).one()

    return Response("Status of thunder{0}:<br>Hypervisor: {1}<br>Status: {2}".format(request.matchdict["thunder_id"], thunder.hypervisor, thunder.status))

def check_status(request):
    session = DBSession()
    thunder = session.query(Thunder).filter(Thunder.id == request.matchdict["thunder_id"]).one()

    thunder.status = do_check_status(thunder)

    session.add(thunder)
    session.flush()
    transaction.commit()

    thunder = session.query(Thunder).filter(Thunder.id == request.matchdict["thunder_id"]).one()

    return Response("Status of thunder{0}:<br>Hypervisor: {1}<br>Status: {2}".format(request.matchdict["thunder_id"], thunder.hypervisor, thunder.status))


def list(request):
    session = DBSession()
    thunders = session.query(Thunder).all()

    return Response(unicode(thunders))

def install(request):
    session = DBSession()
    thunder = session.query(Thunder).filter(Thunder.id == request.matchdict["thunder_id"]).one()
    thunder.status = u"installing"
    thunder.hypervisor = request.matchdict["hypervisor"]
    session.add(thunder)
    session.flush()
    transaction.commit()

    do_install(thunder,request.matchdict["hypervisor"])

    return Response("Installing hypervisor {0} on thunder {1}...".format(request.matchdict["hypervisor"], request.matchdict["thunder_id"]))

def poweron(request):
    session = DBSession()
    tid = request.matchdict["thunder_id"]
    thunder = session.query(Thunder).filter(Thunder.id == tid).one()
    thunder.status = u"poweringon"
    session.add(thunder)
    session.flush()
    transaction.commit()

    do_poweron(thunder)

    return Response("Poweron thunder {0}".format(request.matchdict["thunder_id"]))

def poweroff(request):
    session = DBSession()
    tid = request.matchdict["thunder_id"]
    thunder = session.query(Thunder).filter(Thunder.id == tid).one()
    thunder.status = u"poweringoff"
    session.add(thunder)
    session.flush()
    transaction.commit()

    do_poweroff(thunder)

    return Response("Poweroff thunder{0}".format(request.matchdict["thunder_id"]))

def reboot(request):
    session = DBSession()
    tid = request.matchdict["thunder_id"]
    thunder = session.query(Thunder).filter(Thunder.id == tid).one()
    thunder.status = u"rebooting"
    session.add(thunder)
    session.flush()
    transaction.commit()

    do_reboot(thunder)

    return Response("Rebooting thunder {0}".format(request.matchdict["thunder_id"]))
