import rndom
import time
from datetime import datetime

# Function to generate random transaction
def generate_transaction():
    transaction = {
        "transaction_id": random.randint(100000, 999999),
        "amount": round(random.uniform(1, 5000), 2),  # amount between $1 and $5000
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "device_country": random.choice(["US", "IN", "UK", "CN", "RU"]),
        "hour": datetime.now().hour
    }
    return transaction

# Simple fraud detection rules
def is_suspicious(transaction):
    if transaction["amount"] > 3000:
        return True, "High amount"
    if transaction["hour"] < 6 or transaction["hour"] > 22:
        return True, "Odd hour"
    if transaction["device_country"] not in ["US", "IN", "UK"]:
        return True, "Foreign device"
    return False, ""

def main():
    print("Starting Real-time Transaction Monitoring Simulator...\n")
    try:
        while True:
            txn = generate_transaction()
            suspicious, reason = is_suspicious(txn)

            if suspicious:
                print(f"[ALERT] Suspicious Transaction Detected! ID: {txn['transaction_id']}, "
                      f"Amount: ${txn['amount']}, Time: {txn['timestamp']}, Reason: {reason}")
            else:
                print(f"Transaction OK: ID {txn['transaction_id']}, Amount ${txn['amount']} at {txn['timestamp']}")

            time.sleep(2)  # simulate delay between transactions

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

if __name__ == "__main__":
    main()
