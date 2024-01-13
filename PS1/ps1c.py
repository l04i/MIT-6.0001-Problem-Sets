annual_salary = float(input('Enter your annual salary: '))


total_cost = 1000000
portion_down_payment = 0.25 
down_payment = total_cost * portion_down_payment
semi_annual_raise = 0.07
current_savings = 0
r=0.04
num_of_months=36
monthly_salary = annual_salary / 12
low = 0.00
high = 1
portion_saved = (low + high) / 2
monthly_deposit = monthly_salary * portion_saved
steps = 0 
  

while abs(current_savings - down_payment) > 100:
    print(portion_saved)
    steps += 1
    for i in range(1,num_of_months+1):
        current_savings *= 1 + r/12
        current_savings += monthly_deposit
        
        if num_of_months % 6 == 0 :
            annual_salary *= 1 + semi_annual_raise
            monthly_salary = annual_salary / 12
            monthly_deposit = monthly_salary * portion_saved
            
            
    
    if current_savings > down_payment:
        high = portion_saved
    else:
        low = portion_saved
    portion_saved = (low + high) / 2
    portion_saved = round(portion_saved,4)



print('The saving percentage is',portion_saved)
print('It was found after',steps,'steps')