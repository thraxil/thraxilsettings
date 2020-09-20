import os.path
import sys


def common(**kwargs):
    app = kwargs['app']
    base = kwargs['base']
    cloudfront = kwargs['cloudfront']

    # have to pull in anything that we'll be changing
    STATIC_ROOT = kwargs['STATIC_ROOT']
    INSTALLED_APPS = kwargs['INSTALLED_APPS']

    MEDIA_ROOT = '/var/www/' + app + '/uploads/'

    # put any static media here to override app served static media
    STATICMEDIA_MOUNTS = [
        ('/sitemedia', '/var/www/' + app + '/' + app + '/sitemedia'),
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': app,
            'HOST': '',
            'PORT': 6432,
            'USER': '',
            'PASSWORD': '',
            'ATOMIC_REQUESTS': True,
        }
    }

    COMPRESS_ROOT = os.path.join(base, "../media")
    DEBUG = False

    AWS_S3_CUSTOM_DOMAIN = cloudfront
    AWS_STORAGE_BUCKET_NAME = "thraxil-" + app + "-static-prod"
    AWS_PRELOAD_METADATA = True
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    S3_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
    STATIC_URL = 'https://%s/media/' % AWS_S3_CUSTOM_DOMAIN
    COMPRESS_ENABLED = True
    COMPRESS_OFFLINE = True
    COMPRESS_ROOT = STATIC_ROOT
    COMPRESS_URL = STATIC_URL
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = S3_URL + '/media/'
    COMPRESS_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_QUERYSTRING_AUTH = False
    return locals()
