import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from classbasedview.ecom import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
})
