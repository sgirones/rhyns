from pyramid.config import Configurator
from sqlalchemy import engine_from_config
import paramiko


from rhyns.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'rhyns:static')
    config.add_route('home', '/', view='rhyns.views.home', view_renderer='string')
    config.add_route('status', '/thunder/{thunder_id}/status', view='rhyns.views.status', view_renderer='string')
    config.add_route('check_status', '/thunder/{thunder_id}/check_status', view='rhyns.views.check_status', view_renderer='string')
    config.add_route('list', '/thunder/list', view='rhyns.views.list', view_renderer='string')
    config.add_route('install', '/thunder/{thunder_id}/install/{hypervisor}', view='rhyns.views.install', view_renderer='string')
    config.add_route('poweron', '/thunder/{thunder_id}/poweron', view='rhyns.views.poweron', view_renderer='string')
    config.add_route('poweroff', '/thunder/{thunder_id}/poweroff', view='rhyns.views.poweroff', view_renderer='string')
    config.add_route('reboot', '/thunder/{thunder_id}/reboot', view='rhyns.views.reboot', view_renderer='string')
    return config.make_wsgi_app()
