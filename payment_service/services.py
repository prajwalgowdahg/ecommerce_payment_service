from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from payment_service.models import Payment

async def process_payment(payment_request, db: AsyncSession):
    # Simulate a successful payment
    payment = Payment(
        order_id=payment_request.order_id,
        amount=payment_request.amount,
        currency=payment_request.currency,
        payment_status="success"
    )
    print(payment,"test")
    db.add(payment)
    db.commit()
    db.refresh(payment)
    print(payment,"payment done")
    return payment

# async def get_payment_status(order_id: str, db: AsyncSession):
#     result = db.query(Payment).filter(Payment.order_id == order_id)
#     return result
    
async def get_payment_status(order_id: str, db: AsyncSession):
    # Use `select` to query the database
    query = select(Payment).filter(Payment.order_id == order_id)
    result =  db.execute(query)
    payment = result.scalars().first()

    if not payment:
        return {"error": "Payment not found"}
    
    # Return a dictionary representation of the payment
    return {
        "id": payment.id,
        "order_id": payment.order_id,
        "amount": payment.amount,
        "currency": payment.currency,
        "payment_status": payment.payment_status,
    }