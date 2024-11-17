from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from payment_service.database import get_db, engine
from payment_service.models import Base
from payment_service.schemas import PaymentRequest, PaymentResponse
from payment_service.services import process_payment, get_payment_status
from payment_service import models,database
app = FastAPI()
import pdb;
# Create the tables in the database
models.Base.metadata.create_all(bind=database.engine)

@app.post("/payments/", response_model=PaymentResponse)
async def create_payment(payment_request: PaymentRequest, db: AsyncSession = Depends(get_db)):
    try:
        #ßpdb.set_trace()
        print("hello here")
        payment = await process_payment(payment_request, db)
        print(payment,"result")
        return {
            "id": payment.id,
            "order_id": payment.order_id,
            "amount": payment.amount,
            "currency": payment.currency,
            "payment_status": payment.payment_status
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/payments/{order_id}")
async def get_payment(order_id: str, db: AsyncSession = Depends(get_db)):
    payment_status = await get_payment_status(order_id, db)
    if "error" in payment_status:
        raise HTTPException(status_code=404, detail=payment_status["error"])
    return payment_status
