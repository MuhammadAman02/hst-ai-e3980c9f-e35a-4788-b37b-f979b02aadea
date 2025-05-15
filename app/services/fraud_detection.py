from app.models.transaction import Transaction

def detect_fraud(transaction: Transaction) -> bool:
    # This is a very simple fraud detection rule
    # In a real system, you'd use more sophisticated methods
    if transaction.amount > 1000 and transaction.merchant.lower() not in ["amazon", "walmart", "target"]:
        return True
    return False