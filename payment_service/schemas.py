from pydantic import BaseModel
from typing import Optional
class PaymentRequest(BaseModel):
    order_id: str
    amount: float
    currency: str = "usd"
    payment_status: Optional[str]="success"

class PaymentResponse(BaseModel):
    id: int
    order_id: str
    amount: float
    currency: str
    payment_status: str
