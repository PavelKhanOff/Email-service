import os


# Middleware
MIDDLEWARE_HOST = os.environ.get("MIDDLEWARE_HOST", "middleware-service")
MIDDLEWARE_PORT = os.environ.get("MIDDLEWARE_PORT", 6000)
PROTOCOL = 'http'
URL_CHECK_SUPER_USER = os.environ.get(
    "URL_CHECK_SUPER_USER", 'middleware/check_superuser'
)
MIDDLEWARE_URL_CHECK_SUPER_USER = (
    f'{PROTOCOL}://{MIDDLEWARE_HOST}:{MIDDLEWARE_PORT}/{URL_CHECK_SUPER_USER}'
)

# MAIL_SETTINGS
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_FROM = os.getenv('MAIL_FROM')
MAIL_PORT = int(os.getenv('MAIL_PORT'))
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_FROM_NAME = os.getenv('MAIN_FROM_NAME')
TEMPLATE_FOLDER = os.getenv('TEMPLATE_FOLDER')

# Celery Settings
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_BACKEND_URL = os.getenv(
    'CELERY_BACKEND_URL',
    "sentinel://sentinel-0.sentinel.default.svc.cluster.local:5000/0;"
    "sentinel://sentinel-1.sentinel.default.svc.cluster.local:5000/0;"
    "sentinel://sentinel-2.sentinel.default.svc.cluster.local:5000/0",
)
# AWS(CDN) SETTINGS
AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_TEMPLATES = os.getenv("BUCKET_TEMPLATES", "templates")
