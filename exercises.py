from decimal import *


#ex1
def generate_postal_code(start_code, finish_code):
    """Return the list of postal codes between start_code and finish_code.
    start_code and finish_code are string"""
    codes = []
    for first_num in range(int(start_code[:2]), int(finish_code[:2])+1):
        for sec_num in range(1,1000):
            if first_num == int(start_code[:2]) and sec_num < int(start_code[3:]):
                continue
            if first_num == int(finish_code[:2]) and sec_num > int(finish_code[3:]):
                break
            codes.append("{}-{}{}".format(first_num, "0"*(3-len(str(sec_num))), sec_num))
    return codes


#ex2
def find_miss_elements(check_list,n):
    """Return the list of missing values between 1 and n.
    check_list is a list 
    n is a int"""
    miss_el = []
    for i in range(1,n+1):
        if i not in check_list:
            miss_el.append(i)
    return miss_el


#ex3
def generate_num(start, stop, step):
    """Return list of Decimal numbers between start and stop where is step.
    start, stop and step are float"""
    numbers = []
    getcontext().prec = 2
    while start <= stop:
        numbers.append(Decimal(start)-Decimal('0.0000')) # 
        start = start + step
    return numbers
