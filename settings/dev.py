from base import *


DEBUG = TEMPLATE_DEBUG = True

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Ubiq_pervasive_dev',
        'USER': 'ubiq',
        'PASSWORD': 'figureitout',
        'HOST': "ubiqdev.coqxmktgaiok.us-west-2.rds.amazonaws.com",
        'PORT': '3306',
    }
}
