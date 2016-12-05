from setuptools import setup, find_packages

setup(
    name="thraxilsettings",
    version="1.0.1",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
    url="https://github.com/thraxil/thraxilsettings",
    description="My common base settings",
    long_description="common settings i use across all my apps",
    install_requires = [
        "django_compressor",
        "django-debug-toolbar",
        "django-waffle",
        "django-jenkins",
        "django-smoketest",
        "django-extensions",
        "django-statsd-mozilla",
        "django-markwhat",
        "django-storages-redux",
        "django-cacheds3storage",
        "statsd",
        "gunicorn",
    ],
    scripts = [],
    license = "BSD",
    platforms = ["any"],
    zip_safe=False,
    package_data = {'' : ['*.*']},
    packages=['thraxilsettings'],
    )
