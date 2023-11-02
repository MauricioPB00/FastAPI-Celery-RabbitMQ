from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Order 
from celery_tasks import processar_pedido


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/receber_dados")
async def receber_dados(order: Order):
    print("Dados recebidos na função receber_dados:", order.dict())

   # tarefa ao Celery para processamento em segundo plano
    task_result = processar_pedido.delay(order.dict())
    
    response_data = {
        "message": "Pedido recebido e está sendo processado em segundo plano. ID da tarefa: " + task_result.id,
        "order": order.dict() 
    }
    
    return response_data
