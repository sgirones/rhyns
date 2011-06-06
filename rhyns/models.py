import transaction

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import Enum





from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Thunder(Base):
    __tablename__ = 'thunders'
    id = Column(Integer, primary_key=True)
    ip = Column(Unicode(15), unique=True)
    ipmiip = Column(Unicode(15), unique=True)
    hypervisor = Column(Enum("esxi","xenserver","kvm","xen","vbox","hyperv","unknown"))
    status = Column(Enum("ok","installing","poweringon","poweringoff","rebooting"))

    def __init__(self, id, ip, ipmiip, hypervisor, status):
        self.id = id
        self.ip = ip
        self.ipmiip = ipmiip
        self.hypervisor = hypervisor
        self.status = status

def populate():
    session = DBSession()
    session.configure

    thunder = Thunder(id=u"1", ip=u"10.60.1.71", ipmiip=u"10.60.10.71", hypervisor=u"esxi", status=u"ok")
    session.add(thunder)
    thunder = Thunder(id=u"3", ip=u"10.60.1.73", ipmiip=u"10.60.10.73", hypervisor=u"esxi", status=u"ok")
    session.add(thunder)
    thunder = Thunder(id=u"4", ip=u"10.60.1.74", ipmiip=u"10.60.10.74", hypervisor=u"xenserver", status=u"ok")
    session.add(thunder)
    thunder = Thunder(id=u"5", ip=u"10.60.1.75", ipmiip=u"10.60.10.75", hypervisor=u"hyperv", status=u"ok")
    session.add(thunder)
    thunder = Thunder(id=u"6", ip=u"10.60.1.76", ipmiip=u"10.60.10.76", hypervisor=u"hyperv", status=u"ok")
    session.add(thunder)
    thunder = Thunder(id=u"7", ip=u"10.60.1.77", ipmiip=u"10.60.10.77", hypervisor=u"xen", status=u"ok")
    session.add(thunder)
    thunder = Thunder(id=u"8", ip=u"10.60.1.78", ipmiip=u"10.60.10.78", hypervisor=u"kvm", status=u"ok")
    session.add(thunder)
    thunder = Thunder(id=u"9", ip=u"10.60.1.79", ipmiip=u"10.60.10.79", hypervisor=u"vbox", status=u"ok")
    session.add(thunder)
    thunder = Thunder(id=u"10", ip=u"10.60.1.80", ipmiip=u"10.60.10.80", hypervisor=u"xenserver", status=u"ok")
    session.add(thunder)
    thunder = Thunder(id=u"11", ip=u"10.60.1.81", ipmiip=u"10.60.10.81", hypervisor=u"xen", status=u"ok")
    session.add(thunder)

    session.flush()
    transaction.commit()
    
def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Thunder.metadata.drop_all(engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        populate()
    except IntegrityError:
        DBSession.rollback()
