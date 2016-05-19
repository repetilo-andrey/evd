from importd import d
from config import *

d(
    ALLOWED_HOSTS=['*'],
    DEBUG=True,
    INSTALLED_APPS=["app"],
    MIDDLEWARE_CLASSES=['app.views.UrlsMiddleware'],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': HOST
        }
    }
)

if __name__ == "__main__":
    d.main()
