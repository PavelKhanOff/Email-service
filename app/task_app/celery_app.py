from celery import Celery
import eduone_mail.app.settings.config as Envs

# celery_pool_asyncio importing is optional
# It imports when you run worker or beat if you define pool or scheduler
# but it does not imports when you open REPL or when you run web application.
# If you want to apply monkey patches anyway to make identical environment
# when you use REPL or run web application app it's good idea to import
# celery_pool_asyncio module
import celery_pool_asyncio  # noqa

# Sometimes noqa does not disable linter (Spyder IDE)
celery_pool_asyncio.__package__


app = Celery(
    "worker_1",
    backend=Envs.CELERY_BACKEND_URL,
    broker=Envs.CELERY_BROKER_URL,
)
app.autodiscover_tasks(['eduone_mail.app.core'])
app.conf.result_backend_transport_options = {'master_name': "mymaster"}
