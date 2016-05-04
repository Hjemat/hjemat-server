# your local dev settings go here.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hjemat',
        'USER': 'hjemat_user',
        'PASSWORD': 'hjematfisk',
        'HOST': 'localhost',
        'PORT': '',
    }
}

CORS_ORIGIN_ALLOW_ALL = True
