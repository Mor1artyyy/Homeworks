class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        a = f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
        return a

    def go_to(self, new_floor):
        new_floor = int(input("Введите на какой этаж едем: "))
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Извините, но такого этажа не существует!!!")
        elif new_floor == 1:
            print("Вы и так на первом этаже!")
        else:
            for i in range (1, new_floor + 1):
                print(i)
            print(f'Лифт приехал на {new_floor} этаж!')


h1 = House("ЖК Яблоневый", 15)
h2= House("ул.Краснооктябрьская", 9)
print("---------------------------------------------")
print(h1)
print("---------------------------------------------")
print("Лифт приехал...")
h1.go_to(None)
print("\n")
print("---------------------------------------------")
print(h2)
print("---------------------------------------------")
print("Лифт приехал...")
h2.go_to(None)

