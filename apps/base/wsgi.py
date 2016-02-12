"""
WSGI config for saja_expo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
from os.path import join, dirname, abspath
import envdir

envdir.read(join(dirname(dirname(dirname(abspath(__file__)))), 'envs'))

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
