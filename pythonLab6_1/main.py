class Shop():
   def __init__(self, shop_name, store_type):
       self.shop_name = shop_name
       self.store_type = store_type
       self.number_of_units = 0

   def describe_shop(self):
        print("Назва магазину:"+self.shop_name + ", тип магазину:" + self.store_type )

   def open_shop(self):
        print("Магазин відритий")

   def set_number_of_units(self):
       number = int(input("Введіть кількість видів товар:"))
       print(number)
store = Shop("Епіцентер", "Будівельний")
print(store.shop_name)
print(store.store_type)
store.set_number_of_units()
store.describe_shop()
store.open_shop()
Shop1 = Shop("Еко", "продуктовий")
Shop1.describe_shop()
Shop2 = Shop("Дніпро-М", "побутовий")
Shop2.describe_shop()
Shop3 = Shop("Кошик", "продуктовий")
Shop3.describe_shop()
store = Shop("Епіцентер", "Будівельний")
print(store.number_of_units)
store.number_of_units = 120
print(store.number_of_units)




def increment_number_of_units(self, num):
    self.num_species += num
    store.increment_number_of_units(100)

