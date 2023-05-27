number = 0
freading = open('numbers.txt', 'rt' )
frecord = open('sum_numbers.txt', 'wt')
while True:
    line = freading.readline()
    if not line:
        break
    number += int(line)
a = frecord.write(str(number))
frecord.close()
freading.close()
print(number)

