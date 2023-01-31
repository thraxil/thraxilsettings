import os.path
import sys


def common(**kwargs):
    app = kwargs['app']
    base = kwargs['base']

    DEBUG = True

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

    if 'test' in sys.argv:
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

    ALLOWED_HOSTS = ['localhost']

    USE_TZ = True
    TIME_ZONE = 'America/New_York'
    LANGUAGE_CODE = 'en-us'
    SITE_ID = 1
    USE_I18N = False
    MEDIA_ROOT = "/var/www/" + app + "/uploads/"
    MEDIA_URL = '/uploads/'
    SECRET_KEY = 'you must override this'
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS':  [
                "/var/www/" + app + "/templates/",
                os.path.join(base, "templates"),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    MIDDLEWARE = [
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'waffle.middleware.WaffleMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]

    ROOT_URLCONF = app + '.urls'

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
        'smoketest',
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
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
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
    SESSION_COOKIE_AGE = 60 * 60 * 24 * 265 * 5

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
    }

    return locals()
