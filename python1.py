# Define the balance
balance = 500  # You can change this value to test different scenarios

# Define the amount you want to withdraw
withdraw_amount = 300

# Check if the balance is sufficient for the withdrawal
if balance >= withdraw_amount:
    # Calculate the new balance after withdrawal
    new_balance = balance - withdraw_amount
    print(f"Withdrawal successful. New balance is ${new_balance}.")
else:
    # If the balance is insufficient
    print("Insufficient funds. Withdrawal cannot be processed.")



num  