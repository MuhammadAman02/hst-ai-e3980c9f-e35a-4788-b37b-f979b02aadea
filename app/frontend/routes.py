from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.models.transaction import Transaction
from app.services.fraud_detection import detect_fraud

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/check-transaction")
async def check_transaction(
    request: Request,
    amount: float = Form(...),
    merchant: str = Form(...),
    card_number: str = Form(...)
):
    transaction = Transaction(amount=amount, merchant=merchant, card_number=card_number)
    is_fraudulent = detect_fraud(transaction)
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "transaction": transaction, "is_fraudulent": is_fraudulent}
    )