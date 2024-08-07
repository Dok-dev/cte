import os
from pathlib import Path
import ast

# Базовая директория проекта
# BASE_DIR = "/app"
BASE_DIR = Path(__file__).resolve().parent.parent

SITE_ID = 1

# Секретный ключ для использования в производственной среде
SECRET_KEY = os.getenv('SITE_SECRET_KEY', 'not')

# Режим отладки (не включайте в производственной среде)
# DEBUG = True
DEBUG = ast.literal_eval(os.getenv('DEBUG', 'True'))

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'exampleprogect.loc', '192.168.59.2']



# Статические файлы (CSS, JavaScript, Images)
STATIC_URL = 'static/' # URL в запросах
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # Директория выгрузки статики для имспрользования Nginx
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app_static'),
]

# Медиа файлы
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL конфигурация
ROOT_URLCONF = 'cte.urls'

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cte',
        'USER': 'cte_user',
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': '10.0.0.12',
        'PORT': '5432',
        # 'NAME': os.getenv('POSTGRES_DB', 'my_database'),
        # 'USER': os.getenv('POSTGRES_USER', 'my_user'),
        # 'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        # 'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# WSGI приложение
WSGI_APPLICATION = 'cte.wsgi.application'

# Приложения Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # Фреймворк аутентификации и моделей по умолчанию.
    'django.contrib.contenttypes', # Django контент-типовая система (даёт разрешения, связанные с моделями).
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'projects',
    'accounts',
    'django_email_verification',
]

# Промежуточное ПО
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # Управление сессиями между запросами
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Связывает пользователей, использующих сессии, запросами.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]


# Настройки REST framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Настройки Dj-rest-auth
REST_USE_JWT = True

# Configure Simple JWT
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# AUTH_USER_MODEL = 'accounts.CustomUser'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# Настройки Django Allauth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Настройки электронной почты для Allauth
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Языки и время
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Show all send e-mails in console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# функция, которая сделает пользователя активным
# после того, как он перейдет по ссылке
def verified_callback(user):
    user.is_active = True

EMAIL_VERIFIED_CALLBACK = verified_callback

# тема письма
EMAIL_MAIL_SUBJECT = 'Confirm your email'
# шаблон письма в html
EMAIL_MAIL_HTML = 'registration/mail_body.html'
# текстовый шаблон
EMAIL_MAIL_PLAIN = 'registration/mail_body.txt'
# время жизни ссылки
EMAIL_MAIL_TOKEN_LIFE = 60 * 60
# шаблон, который увидят после перехода по ссылке
EMAIL_MAIL_PAGE_TEMPLATE = 'registration/confirm_template.html'
# домен для использования в ссылке
EMAIL_PAGE_DOMAIN = 'http://mydomain.com/'
EMAIL_MULTI_USER = True

# настройки вашего SMTP сервера
EMAIL_HOST = os.getenv('MAIL_SERVER')
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_FROM_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('MAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
