annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise= float(input('Enter the semiannual raise, as a decimal: '))

portion_down_payment = 0.25 
down_payment = total_cost * portion_down_payment
current_savings = 0
r=0.04
num_of_months=0
monthly_salary = annual_salary / 12
monthly_deposit = monthly_salary * portion_saved


while current_savings < down_payment:
        num_of_months += 1
        current_savings *= 1 + r/12
        current_savings += monthly_deposit
        if num_of_months % 6 == 0:
            annual_salary *= 1 + semi_annual_raise
            monthly_salary = annual_salary / 12 
            monthly_deposit = monthly_salary * portion_saved
            
    
        
        
print('The number of months required',num_of_months)