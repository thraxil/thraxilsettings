# flake8: noqa
# docker-compose settings doesn't really have to do much
# since it's a dev environment and is mostly covered by
# settings_shared. mostly, it just has to set up some
# defaults
import os
import sys


def common(**kwargs):
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
            'ATOMIC_REQUESTS': True,
        }
    }
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
    BROKER_URL = "amqp://guest:guest@rabbitmq:5672/"
    CELERY_BROKER_URL = BROKER_URL
    return locals()
