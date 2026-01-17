class Turtle:
    def __init__(self, x=0, y=0, s=1):
        """
        Инициализация черепашки с начальными координатами и шагом.
        
        Args:
            x: начальная координата x (по умолчанию 0)
            y: начальная координата y (по умолчанию 0)
            s: размер шага (по умолчанию 1)
        """
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        """Увеличивает y на s"""
        self.y += self.s
    
    def go_down(self):
        """Уменьшает y на s"""
        self.y -= self.s
    
    def go_left(self):
        """Уменьшает x на s"""
        self.x -= self.s
    
    def go_right(self):
        """Увеличивает x на s"""
        self.x += self.s
    
    def evolve(self):
        """Увеличивает s на 1"""
        self.s += 1
    
    def degrade(self):
        """
        Уменьшает s на 1.
        Выкидывает ошибку, если s может стать ≤ 0.
        """
        if self.s <= 1:
            raise ValueError("Нельзя уменьшить шаг, так как он станет ≤ 0")
        self.s -= 1
    
    def count_moves(self, x2, y2):
        """
        Возвращает минимальное количество действий для перемещения от текущей позиции до (x2, y2).
        
        Args:
            x2: целевая координата x
            y2: целевая координата y
            
        Returns:
            Минимальное количество ходов или None, если достижение невозможно
        """
        # Вычисляем разницу по осям
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        # Если шаг равен 0, движение невозможно
        if self.s == 0:
            return None
        
        # Вычисляем минимальное количество ходов
        # Каждый ход может переместить нас на s клеток по одной из осей
        moves_x = dx // self.s + (1 if dx % self.s != 0 else 0)
        moves_y = dy // self.s + (1 if dy % self.s != 0 else 0)
        
        return moves_x + moves_y
    
    def __str__(self):
        """Строковое представление черепашки"""
        return f"Черепашка: позиция ({self.x}, {self.y}), шаг {self.s}"




turtle = Turtle()
s = 1
while s == 1:
    print(f"Начальное состояние: {turtle}")
    print(f'Выберите действие\n 1)двигать черепашку вверх\n 2)Двигать черепашку вниз\n 3)Двигать черепашку в лево\n 4)Двигать черепашку в право')
    print(f' 5)Увеличивает шаг черепашки на 1\n 6)Уменьшает шаг черепашки на 1\n 7)Расчитать за сколько ходов черепашка переместится на позицию (2, 2)\n 8)Выйти из программы')
    
    i = int(input())
    if i == 1:
        turtle.go_up()
        print(f"После go_up: {turtle}")
    
    elif i == 2:    
        turtle.go_down()
        print(f"После go_down: {turtle}")
    
    elif i == 3:
        turtle.go_left()
        print(f"После go_left: {turtle}")
    
    elif i == 4:
        turtle.go_right()
        print(f"После go_right: {turtle}")
        
    elif i == 5:
        turtle.evolve()
        print(f"После evolve: {turtle}")
    
    elif i == 6:
        turtle.degrade()
        print(f"После degrade: {turtle}")   
    
    elif i == 7: 
        moves = turtle.count_moves(2, 2)
        print(f"Минимальное количество ходов до (2, 2): {moves}")       
        
    s = int(input(' 1)Продолжить\n 2)Закрыть программу\n'))           





