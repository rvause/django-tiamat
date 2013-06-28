INSTALLED_APPS = (
    'tiamat',
    'tiamat.tests',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

SECRET_KEY = 'ASECRETKEY'

URL_ENCODER_KEY = 'AURLENCODERKEYTHATISQUITELONG'
