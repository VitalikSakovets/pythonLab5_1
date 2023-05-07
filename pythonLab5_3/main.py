def whole_numbers(q,result):
    while q != 0:
        r = (q % 2)
        result.insert(0, r)
        q = int(q/2)
    print(result)
result = []
q = 123441
whole_numbers(q,result)

def fractional_numbers(q,result):
    while q != 0:
        r = (q %2)
        result.insert(0, r)
        q = int(q/2)
    print(result)
result = []
q = 0.3441
fractional_numbers(q,result)
print(0.3441%2)
