# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
total_paid = 0.0
month = 0



while principal > payment:
    if (month >= extra_payment_start_month) & (month <= extra_payment_end_month):   
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:    
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    print (month+1, round(total_paid,2), round(principal,2))
    month = month + 1
    
print('Total paid', round(total_paid,2), 'Month', month, 'rest', round(principal,2))

