data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for transaction in transactions:
    amount, statement = transaction
    print(f"${amount} - {statement}")

print_transactions(data)

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(total_deposited)
  withdraw = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdraw = sum(withdraw)
  print(total_withdraw)
  balance = total_deposited + total_withdraw
  print(balance)

print_summary(data)

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(largest_withdrawal)
  print(largest_deposit)

  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposit = sum(deposits)
  if len(deposits) > 0:
    average_deposit = total_deposit / len(deposits)
  else:
    average_deposit = 0
  print(average_deposit)

  withdraw = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdraw = sum(withdraw)
  if len(withdraw) > 0:
    average_withdraw = total_withdraw / len(withdraw)
  else:
    average_withdraw = 0
  print(average_withdraw)

analyze_transactions(data)

while True:
  print("\nChoose an option:")
  print("1. Print summary (type 'print')")
  print("2. Analyze transactions (type 'analyze')")
  print("3. Stop program (type 'stop')")
  choice = input("Enter your option: ")
  if choice.lower() == "print":
    print_summary(data)
  elif choice.lower() == "analyze":
    analyze_transactions(data)
  elif choice.lower() == "stop":
    break
  else:
    print("Invalid choice")