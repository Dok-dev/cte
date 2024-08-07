import os
import sys
import logging
from django.core.wsgi import get_wsgi_application

# Установите переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cte.settings')

# Настройте логирование в stdout
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# Создайте WSGI-приложение
try:
    application = get_wsgi_application()
except Exception as e:
    logging.error('Failed to create WSGI application', exc_info=True)
    raise e


# from logging.handlers import RotatingFileHandler

# # Настройте логирование файл
# log_directory = '/var/www/logs/cte'
# if not os.path.exists(log_directory):
#     os.makedirs(log_directory)

# log_file = os.path.join(log_directory, 'cte.log')

# handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# handler.setFormatter(formatter)

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# logger.addHandler(handler)
