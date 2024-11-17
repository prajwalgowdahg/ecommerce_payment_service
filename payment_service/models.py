from sqlalchemy import Column, Integer, String, Float, Boolean
from payment_service.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, unique=True, nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="usd")
    payment_status = Column(String, default="pending")  # pending, success, failed
