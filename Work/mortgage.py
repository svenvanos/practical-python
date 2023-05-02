# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

month = 0

while principal > 0:
    month += 1
    
    principal = principal * (1 + rate / 12) - payment
    total_paid += payment
    
    # when there is extra payment
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    
    # for the final month if too much is paid
    if principal < 0:
        total_paid += principal
        principal = 0
    
    print(f"{month} \t {round(total_paid, 2)} \t {round(principal, 2)}")
    
print(f"Total paid {round(total_paid, 1)}")
print(f"Months {month}")