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
import rhyns.thunders_control
DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Thunder(Base):
    __tablename__ = 'thunders'
    id = Column(Integer, primary_key=True)
    ip = Column(Unicode(15), unique=True)
    ipmiip = Column(Unicode(15), unique=True)
    hypervisor = Column(Enum("esxi","xenserver","kvm","xen","vbox","hyperv","unknown","none"))
    status = Column(Enum("ok","installing","poweringon","poweringoff","rebooting","locked"))
    power = Column(Unicode(15))

    def __init__(self, id, ip, ipmiip, hypervisor, status, power):
        self.id = id
        self.ip = ip
        self.ipmiip = ipmiip
        self.hypervisor = hypervisor
        self.status = status
        self.power = power

def populate():
    t = [1,3,4,5,6,7,8,9,10,11]  # thunders 0wned 
    session = DBSession()
    session.configure
    
    print("== POPULATING THUNDERS ==")
    for i in t:
    
      thunder = Thunder(id=unicode(i), ip=unicode("10.60.1."+str(70+i)), ipmiip=unicode("10.60.1.1"+str(70+i)), hypervisor=u"none", status=u"ok", power=u"on")
      thunder.hypervisor = rhyns.thunders_control.do_check_hypervisor(thunder)
      thunder.power = rhyns.thunders_control.do_check_power(thunder)
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
