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
    thunders = session.query(Thunder).all()

    # for t in thunders:
    #
    #    t.hypervisor = do_check_hypervisor(t)
    #     session.add(t)
    # session.flush()
    # transaction.commit()

    # thunder = session.query(Thunder).filter(Thunder.id == "1").one()
    # thunders = session.query(Thunder).all()

    return  {'project':'thunderdome', 'thunders':thunders}



def status(request):
    session = DBSession()
    thunder = session.query(Thunder).filter(Thunder.id == request.matchdict["thunder_id"]).one()

    return Response("Status of thunder{0}:<br>Hypervisor: {1}<br>Status: {2}".format(request.matchdict["thunder_id"], thunder.hypervisor, thunder.status))

@view_config(renderer='list.mako')
def check_status(request):
    session = DBSession()
    thunder = session.query(Thunder).filter(Thunder.id == request.matchdict["thunder_id"]).one()
    thunder.hypervisor = do_check_hypervisor(thunder)
    thunder.power = do_check_power(thunder)
    if (thunder.status == u"installing" and thunder.hypervisor != u"unknown") :
        thunder.status = u'ok'

    session.add(thunder)
    session.flush()
    transaction.commit()
    res = "Refreshing Thunder{0}".format(request.matchdict["thunder_id"]) 
    # thunders = session.query(Thunder).all()
    return {'project':'thunders','message':res}
    # return Response("Status of thunder{0}:<br>Hypervisor: {1}<br>Status: {2}".format(request.matchdict["thunder_id"], thunder.hypervisor, thunder.status))

def lock(request):
    session = DBSession()
    tid = request.matchdict["thunder_id"]
    thunder = session.query(Thunder).filter(Thunder.id == tid).one()
    thunder.status = u"locked"
    session.add(thunder)
    session.flush()
    transaction.commit()

    return {'project':'thunders','message':"Locked thunder{0}".format(request.matchdict["thunder_id"])}
    # return Response("Locked thunder {0}".format(request.matchdict["thunder_id"]))

def unlock(request):
    session = DBSession()
    tid = request.matchdict["thunder_id"]
    thunder = session.query(Thunder).filter(Thunder.id == tid).one()
    thunder.status = u"ok"
    session.add(thunder)
    session.flush()
    transaction.commit()
    # return Response("Unlocked thunder{0}".format(request.matchdict["thunder_id"]))
    return {'project':'thunders','message':"Unlocked thunder{0}".format(request.matchdict["thunder_id"])}


def list(request):
    session = DBSession()
    thunders = session.query(Thunder).all()

    return Response(unicode(thunders))

def install(request):
    session = DBSession()
    thunder = session.query(Thunder).filter(Thunder.id == request.matchdict["thunder_id"]).one()
    if thunder.status != "locked":
      thunder.status = u"installing"
      thunder.hypervisor = request.matchdict["hypervisor"]
      session.add(thunder)
      session.flush()
      transaction.commit()

      thunder = session.query(Thunder).filter(Thunder.id == request.matchdict["thunder_id"]).one()
      do_install(thunder.ipmiip,request.matchdict["hypervisor"])
      res = "Installing hypervisor {0} on thunder {1}...".format(request.matchdict["hypervisor"], request.matchdict["thunder_id"])
    else:
      res = "Thunder {0} locked!".format(request.matchdict["thunder_id"])
    return {'project':'thunders','message':res}

def poweron(request):
    session = DBSession()
    tid = request.matchdict["thunder_id"]
    thunder = session.query(Thunder).filter(Thunder.id == tid).one()
    if thunder.status != "locked":
      do_poweron(thunder)
      thunder.status = u"poweringon"
      session.add(thunder)
      session.flush()
      transaction.commit()
      res = "Powering on thunder {0}...".format(request.matchdict["thunder_id"])
    else:
      res = "Thunder {0} locked!".format(request.matchdict["thunder_id"])
    return {'project':'thunders','message':res}

def poweroff(request):
    session = DBSession()
    tid = request.matchdict["thunder_id"]
    thunder = session.query(Thunder).filter(Thunder.id == tid).one()
    if thunder.status != "locked":
      do_poweroff(thunder)
      thunder.status = u"poweringoff"
      session.add(thunder)
      session.flush()
      transaction.commit()
      res = "Powering off thunder{0}...".format(request.matchdict["thunder_id"])
    else:
      res = "Thunder{0} locked!".format(request.matchdict["thunder_id"])
    return {'project':'thunders','message':res}

def reboot(request):
    session = DBSession()
    tid = request.matchdict["thunder_id"]
    thunder = session.query(Thunder).filter(Thunder.id == tid).one()
    if thunder.status != "locked":
      do_reboot(thunder)
      thunder.status = u"rebooting"
      session.add(thunder)
      session.flush()
      transaction.commit()
      res = "Rebooting thunder{0}...".format(request.matchdict["thunder_id"])
    else:
      res = "Thunder{0} locked!".format(request.matchdict["thunder_id"])
    return {'project':'thunders','message':res}

