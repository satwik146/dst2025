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
print(f'taxable income: = {taxableIncome}')

print('-' * 27)
print('%12s %s'% ('salaryRange', 'Tax percentage'))
print('-' * 27)
print('%7d - %-7d %3d%%' % (0,300000, '0'))
print('%7d - %-7d %3d%%' % (300001,600000, '5'))
print('%7d - %-7d %3d%%' % (600001,900000, '10'))
print('%7d - %-7d %3d%%' % (900001,1200000, '15'))
print('%7d - %-7d %3d%%' % (1200001,1500000, '20'))
print('%7d - %-7s %3d%%' % (1500001,'or more', '30'))