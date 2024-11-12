from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_to_pdf_project.settings')

app = Celery('image_to_pdf_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()