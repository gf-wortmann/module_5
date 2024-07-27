# Домашняя работа по уроку "Специальные методы классов"

class House:
    def __init__(self, name: str, count_of_floors: int):
        self.name = name
        self.count_of_floors = count_of_floors

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

    # def __del__(self):
    #     print(f'{self.name} ruined')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
