# Домашняя работа по уроку "Атрибуты и методы объекта."

class House:
    def __init__(self, name: str, count_of_floors: int):
        self.name = name
        self.count_of_floors = count_of_floors

    def go_to(self, target_floor):
        if target_floor > self.count_of_floors or target_floor < 1:
            print('Такого этажа не существует')
            pass
        else:
            for current_floor in range(1,target_floor+1):
                print(f'Текущий этаж - {current_floor}')


h1 = House('ЖК Горский', 18)
h1.go_to(5)
h2 = House('Домик в деревне', 2)
h2.go_to(10)
