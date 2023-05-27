q = 206.116
a = q - int(q)
q = int(q)
def whole_numbers(q):
    result = ""
    while q != 0:
        r = (q % 2)
        # result.insert(0, r)
        result += str(r)
        q = int(q/2)
    return result
whole_numbers(q)
def fractional_numbers(a):
    res = ""
    while a!=0:
        if a<=1:
           a1 = a * 2
           a = a1 - int(a1)
           number = int(a1-a)
           res += str(number)
    return res
fractional_numbers(a)
print(whole_numbers(q) + ',' + fractional_numbers(a))