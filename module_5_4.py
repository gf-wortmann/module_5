# Домашняя работа по уроку "Перегрузка операторов."

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name: str, count_of_floors: int):
        self.name = name
        self.count_of_floors = count_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но останется в истории')

    def __len__(self):
        return self.count_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.count_of_floors}'

    def go_to(self, target_floor):
        if target_floor > self.count_of_floors or target_floor < 1:
            print('Такого этажа не существует')
            pass
        else:
            for current_floor in range(1, target_floor + 1):
                print(f'Текущий этаж - {current_floor}')

    def __eq__(self, other):
        return self.count_of_floors == other.count_of_floors

    def __lt__(self, other):
        return self.count_of_floors < other.count_of_floors

    def __le__(self, other):
        return self.count_of_floors <= other.count_of_floors

    def __gt__(self, other):
        return self.count_of_floors > other.count_of_floors

    def __ge__(self, other):
        return self.count_of_floors >= other.count_of_floors

    def __ne__(self, other):
        return self.count_of_floors != other.count_of_floors

    def __add__(self, value: int):
        self.count_of_floors += value
        return self

    def __radd__(self, value: int):
        return self.__add__(value)

    def __iadd__(self, value: int):
        return self.__add__(value)

    def __mul__(self, value: int):
        self.count_of_floors *= value
        return self

    def __sub__(self, value: int):
        self.count_of_floors -= value
        return self

    def __rsub__(self, value: int):
        self.count_of_floors = value - self.count_of_floors
        return self

    def __truediv__(self, value: int):
        return self.__floordiv__(value)

    def __floordiv__(self, value: int):
        self.count_of_floors //= value
        return self


h1 = House('ЖК Эльбрус', 30)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# print(h1)
# print(h2)
print(House.houses_history)

del h2
del h3
print(House.houses_history)
