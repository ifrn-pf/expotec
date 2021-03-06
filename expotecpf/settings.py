import environ
from django.urls import reverse_lazy

env_settings = {
    'DEBUG': (bool, True),
    'SECRET_KEY': (str, 'dummy'),
    'ALLOWED_HOSTS': (list, ['*']),
}

root = environ.Path(__file__) - 2
env = environ.Env(**env_settings)

BASE_DIR = root()
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
INTERNAL_IPS = ['127.0.0.1']
FORCE_SCRIPT_NAME = env('FORCE_SCRIPT_NAME', default=None)

INSTALLED_APPS = [
    'eventos',
    'trabalhos',
    'site_content',
    'registration',
    'sfp',
    'crispy_forms',
    'semantic_ui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'sfp.middleware.SfpFallbackMiddleware',
]

ROOT_URLCONF = 'expotecpf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'expotecpf.wsgi.application'

DATABASES = {
    'default': env.db(default='sqlite:///db.sqlite3')
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = env('STATIC_URL', default='/static/')
STATIC_ROOT = env('STATIC_ROOT', default=str(root.path('static')))
MEDIA_URL = env('MEDIA_URL', default='/media/')
MEDIA_ROOT = env('MEDIA_ROOT', default=str(root.path('media')))
AUTH_USER_MODEL = 'eventos.Usuario'
SFP_HANDLE_HOMEPAGE = True
CRISPY_TEMPLATE_PACK = 'semantic-ui'
CRISPY_ALLOWED_TEMPLATE_PACKS = ('semantic-ui',)
REGISTRATION_FORM = 'eventos.forms.RegisterForm'
ACCOUNT_AUTHENTICATED_REGISTRATION_REDIRECTS = True
LOGIN_REDIRECT_URL = reverse_lazy('eventos_area_usuario')
SIMPLE_BACKEND_REDIRECT_URL = LOGIN_REDIRECT_URL
LOGOUT_REDIRECT_URL = reverse_lazy('home')
LOGIN_URL = reverse_lazy('auth_login')
TRABALHOS_POR_INSCRICAO = 2
FILE_UPLOAD_MAX_SIZE = 10 * 1024 * 1024
CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS', default=[])
USE_X_FORWARDED_HOST = env('USE_X_FORWARDED_HOST', default=True)
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default=None)
EMAIL_CONFIG = env.email_url('EMAIL_URL', default='consolemail://')
vars().update(EMAIL_CONFIG)
SITE_ID = 1
