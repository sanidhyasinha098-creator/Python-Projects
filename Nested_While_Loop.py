print("=== ATM Cash Dispenser ===\n")
Total_100 = Total_50 = Total_20 = Total_10 = Total_5 = Total_1 = 0
Customers_Served = 0
Total_Dispensed = 0

Serving = True
while Serving:
    Name = input("Enter your name: ")
    Amount = int(input(f"Hello {Name}! Enter withdrawal amount:  "))
    if Amount <= 0:
        print("Invalid amount. Please enter a positive Value.\n")
        continue

    print(f"\nDispensing ₹{Amount} units for {Name}")
    Remaining_Amount = Amount
    IDX = 1
    while IDX <= 6:
        if IDX == 1: Value = 100
        elif IDX == 2: Value = 50
        elif IDX == 3: Value = 20
        elif IDX == 4: Value = 10
        elif IDX == 5: Value = 5
        else: Value = 1
        Count = Remaining_Amount // Value
        if Count > 0:
            print(f"{Count}x{Value}- Unit note(s) = {Count * Value}")
            Remaining_Amount -= Count * Value
            if Value == 100: Total_100 += Count
            elif Value == 50: Total_50 += Count
            elif Value == 20: Total_20 += Count
            elif Value == 10: Total_10 += Count
            elif Value == 5: Total_5 += Count
            else: Total_1 += Count
        IDX += 1

    Customers_Served += 1
    Total_Dispensed += Amount
    print(f"Transaction completed, {Name}!\n")
    Again = input("Next Customer? (Y/N): ") 
    if Again.lower() != 'y':
        Serving = False

print("\n=== Daily Denomination Report ===")
for slot in range(1, 7):                      # outer for -- one denomination per loop
    if slot == 1: value, total = 100, Total_100
    elif slot == 2: value, total = 50, Total_50
    elif slot == 3: value, total = 20, Total_20
    elif slot == 4: value, total = 10, Total_10
    elif slot == 5: value, total = 5, Total_5
    else: value, total = 1, Total_1
    if total > 0:
        print(f"₹{value}-Unit(s) note dispensed : {total} ", end="")
        for note in range(total):             
            print("=", end="")
        print()

print(f"\nCustomers served : {Customers_Served}")
print(f"Total dispensed  : {Total_Dispensed} units")
print("ATM session closed. Goodbye!")    


