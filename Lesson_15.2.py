#Отределяем родительский класс Transport 
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

#Создаём наследуемый класс Autobus от Transport
class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        # Переопределяем метод с значением по умолчанию 50
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


# Создаем объект класса Autobus
autobus = Autobus("Renaul Logan", 180, 12)

# Вызываем метод seating_capacity без аргументов (используется значение по умолчанию)
print(autobus.seating_capacity())