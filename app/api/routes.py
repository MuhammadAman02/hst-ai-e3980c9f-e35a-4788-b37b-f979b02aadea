from fastapi import APIRouter
from app.models.transaction import Transaction
from app.services.fraud_detection import detect_fraud

router = APIRouter()

@router.post('/detect-fraud')
async def fraud_detection(transaction: Transaction):
    is_fraudulent = detect_fraud(transaction)
    return {"transaction": transaction, "is_fraudulent": is_fraudulent}

@router.get('/ping')
async def ping_pong():
    """A simple ping endpoint."""
    return {"message": "pong!"}