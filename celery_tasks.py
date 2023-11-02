from celery import Celery
from models import Order 
from celeryconfig import broker_url, result_backend

app = Celery(
    'myapp',
    broker=broker_url,
    backend=result_backend
)

@app.task
def processar_pedido(order):
    print("Dados recebidos no processar_pedido:", order)
    # Resto do código
    return order
