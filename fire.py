from threading import Thread
import os
import time

import django
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application


def upvote_reset():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_api_djangorest.settings")
    django.setup()
    from core.models import Upvote

    while True:
        time.sleep(60 * 60 * 24)
        Upvote.objects.all().delete()


if __name__ == "__main__":
    Thread(target=upvote_reset, daemon=True).start()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_task.settings")
    application = get_wsgi_application()
    call_command("runserver", "0.0.0.0:8000")
