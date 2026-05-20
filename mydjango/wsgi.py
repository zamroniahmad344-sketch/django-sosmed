import os
import logging
import traceback
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydjango.settings')

logger = logging.getLogger(__name__)

_application = get_wsgi_application()


def application(environ, start_response):
    """Thin wrapper that logs any unhandled exception before re-raising it."""
    try:
        return _application(environ, start_response)
    except Exception:
        logger.error(
            'Unhandled exception in WSGI application:\n%s',
            traceback.format_exc(),
        )
        raise

