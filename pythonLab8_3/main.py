from datetime import datetime
prizvyshce1 = (input("Введіть прізвище клієнта:"))
name1 = input("Введіть ім'я клієнта:")
data1 = int(input('Введіть рік народження клієнта(гггг): '))
balans1 =float(input("Введіть баланс рахунку в грн:"))
dolar = float(38.40)
balans_user1 = balans1/dolar

data = datetime.now().year
vik1 = data-data1
print("{0} {1} {2} {3} {4} {5}".format(prizvyshce1, name1, vik1,"р. Баланс рахунку", '%.2f' % balans_user1, "$"))

