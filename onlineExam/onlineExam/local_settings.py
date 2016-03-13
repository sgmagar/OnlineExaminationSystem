from settings import *;

DEBUG=True;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onlineexam',
        'USER': 'root',
        'PASSWORD': 'heisenberg',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # 'OPTIONS': {'init_command':'SET storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci'},
        'OPTIONS':{'charset': 'utf8'},
    }
}