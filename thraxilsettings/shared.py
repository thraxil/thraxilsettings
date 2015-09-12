import os.path
import sys


def common(**kwargs):
    app = kwargs['app']
    base = kwargs['base']

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    ADMINS = ()

    MANAGERS = ADMINS

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': app,
            'HOST': '',
            'PORT': 5432,
            'USER': '',
            'PASSWORD': '',
            'ATOMIC_REQUESTS': True,
        }
    }

    if 'test' in sys.argv or 'jenkins' in sys.argv:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
                'HOST': '',
                'PORT': '',
                'USER': '',
                'PASSWORD': '',
                'ATOMIC_REQUESTS': True,
            }
        }

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

    JENKINS_TASKS = (
        'django_jenkins.tasks.run_pylint',
        'django_jenkins.tasks.run_pep8',
        'django_jenkins.tasks.run_pyflakes',
    )

    ALLOWED_HOSTS = ['localhost']

    USE_TZ = True
    TIME_ZONE = 'America/New_York'
    LANGUAGE_CODE = 'en-us'
    SITE_ID = 1
    USE_I18N = False
    MEDIA_ROOT = "/var/www/" + app + "/uploads/"
    MEDIA_URL = '/uploads/'
    SECRET_KEY = 'you must override this'
    TEMPLATE_LOADERS = [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]

    TEMPLATE_CONTEXT_PROCESSORS = [
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.request',
        'django.core.context_processors.static',
    ]

    MIDDLEWARE_CLASSES = [
        'django_statsd.middleware.GraphiteRequestTimingMiddleware',
        'django_statsd.middleware.GraphiteMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'waffle.middleware.WaffleMiddleware',
    ]

    ROOT_URLCONF = app + '.urls'

    TEMPLATE_DIRS = [
        "/var/www/" + app + "/templates/",
        os.path.join(base, "templates"),
    ]

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.flatpages',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'compressor',
        'debug_toolbar',
        'waffle',
        'django_jenkins',
        'smoketest',
        'django_extensions',
        'django_statsd',
        'gunicorn',
        'django_markwhat',
    ]

    STATIC_URL = "/media/"
    STATICFILES_DIRS = [
        os.path.abspath(os.path.join(base, "../media/")),
    ]
    STATIC_ROOT = ""
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    ]

    INTERNAL_IPS = ['127.0.0.1']
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
    ]

    THUMBNAIL_SUBDIR = "thumbs"
    EMAIL_SUBJECT_PREFIX = "[" + app + "] "
    EMAIL_HOST = 'localhost'
    SERVER_EMAIL = app + "@thraxil.org"
    DEFAULT_FROM_EMAIL = SERVER_EMAIL

    # put any static media here to override app served static media
    STATICMEDIA_MOUNTS = [
        ('/sitemedia', 'sitemedia'),
    ]

    COMPRESS_URL = "/media/"
    COMPRESS_ROOT = "media/"

    COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.CSSMinFilter',
    ]

    SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
    SESSION_COOKIE_HTTPONLY = True

    STATSD_CLIENT = 'statsd.client'
    STATSD_PREFIX = app
    STATSD_HOST = '127.0.0.1'
    STATSD_PORT = 8125

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
    }

    return locals()
