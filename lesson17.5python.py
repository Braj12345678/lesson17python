# write a function to calc an employee's salary
def employee(name):
    print(name)
# write a function to calculate an employee's salary
def salary(exp):
    if exp < 2:
        return 25000
    elif exp < 5:
        return 50000
    elif exp < 10:
        return 90000
    else:
        return 120000
employee("Jason")
a = salary(9)
print("Salary for the employee is", a )