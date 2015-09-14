# thraxilsettings

These are my common settings extracted from various apps. I don't
expect this to be useful to anyone but me, but I think the idea is
interesting so perhaps you might like to see it.

The basic issue is that I have a bunch of Django apps that all have
*similar* but obviously not identical settings. If I want to change
something, eg, configuring S3 and Cloudfront for static files, I find
that I have to make a bunch of very similar edits to the config files
of all of them. That is tedious and error-prone.

So I've extracted the common base settings into this package that I
can import into each project and only override what is specific to
that project.

The problem is that quite a few individual settings are based on a
common pattern, but make use of some simple aspect of the individual
app, like the name or base directory to construct it. Eg, in app
'foo', the `DATABASES` setting might be something like:


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'foo',
            'HOST': '',
            'PORT': 5432,
            'USER': '',
            'PASSWORD': '',
        }
    }

Notice the `'foo'` in there as the name of the database. That makes it
really awkward to re-use that stanza across apps. If I just put
everything into `thraxilsettings.shared` and do:

    from thraxilsettings.shared import *


I'd still have to override or tweak the `DATABASES` in every app in
exactly the same way. Better than the original situation, but still
not as clean as I'd like.

Instead, my solution is to package things up in a function that can be
passed parameters and return a dictionary of values, which I can then
stick back into the local symbol table like so:


    from thraxilsettings.shared import common
	locals().update(common(app='foo'))

Mucking with the symbol table like this isn't *exactly* a recommended
best practice in general. It can quickly get confusing and hard to
debug, but in this case, I think the tradeoff is worth it.

I have three separate modules in there: one for the shared settings,
one for a regular "production" deployment, and one that sets up the
base for my current deployment approach inside a docker container that
mostly just pulls in settings from environment variables.

For a full example, this commit shows one of my apps being converted
from the old style to the new `thraxilsettings` style:

https://github.com/thraxil/antisocial/commit/ef6347350668662c05489c30e42a105d3825df67

All those deleted lines of code make me happy!

And here are typical post-conversion `settings_shared.py` and
`settings_docker.py` files from another app:

https://github.com/thraxil/myopica/blob/master/myopica/settings_shared.py

https://github.com/thraxil/myopica/blob/master/myopica/settings_docker.py
