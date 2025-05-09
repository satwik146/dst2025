name = input("Enter your name")
empid = int(input("Enter your emp id"))
monthlyBasicSalary = float(input("Enter your monthly salary"))   
specialAllowance = float(input("Enter monthly allowance"))    
BonusPercentage = float(input("Enter bonus percentage"))   

grossMonthlySalary = monthlyBasicSalary + specialAllowance 
anualBonus = (grossMonthlySalary * 12) * (BonusPercentage / 100) 
annualGrossSalary = (grossMonthlySalary * 12) + anualBonus

print('employee name:', name)
print('employee id:', empid)
print('monthly basic salary:', monthlyBasicSalary)
print('annual gross salary:', annualGrossSalary)

print('%-6s %-15s %-7s %-15s %s' % ('Id', 'Name','Bonus', 'Monthly Salary', 'Annual Salary'))
print('-' * 80)
print('%-6d %-15s %-6.2f %15.2f %.2f ' % (empid, name, BonusPercentage, grossMonthlySalary, annualGrossSalary))

