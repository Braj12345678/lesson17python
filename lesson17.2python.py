def cube(number):
    return number*number*number

def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
print(by_three(9))  
print(by_three(3))