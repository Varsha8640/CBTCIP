# Input variables
name = input("Enter customer name: ")
date = input("Enter date (DD/MM/YYYY): ")
amount = float(input("Enter payment amount: "))
payment_method = input("Enter payment method (Cash/Online): ")

# Generate receipt
print("\nPayment Receipt")
print("----------------")
print(f"Date: {date}")
print(f"Customer Name: {name}")
print(f"Payment Amount: Rs.{amount:.2f}")
print(f"Payment Method: {payment_method}")
print("----------------")
print("Thank you for your payment!")