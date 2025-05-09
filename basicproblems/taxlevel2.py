name = input("Enter your name")
empid = int(input("Enter your emp id"))
monthlyBasicSalary = float(input("Enter your monthly salary"))   
specialAllowance = float(input("Enter monthly allowance"))    
BonusPercentage = float(input("Enter bonus percentage"))   

grossMonthlySalary = monthlyBasicSalary + specialAllowance 
annualBonus = (grossMonthlySalary * 12) * (BonusPercentage / 100) 
annualGrossSalary = (grossMonthlySalary * 12) + annualBonus

standardDeduction = 50000
taxableIncome = annualGrossSalary - standardDeduction
print('taxable income:', taxableIncome)