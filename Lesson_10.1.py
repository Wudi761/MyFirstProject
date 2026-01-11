# Создаем пустой словарь pets
pets = {}

# Функция для правильного склонения слова "год"
def get_age_suffix(age):
    if 11 <= age % 100 <= 19:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

# Запрашиваем количество питомцев для ввода
num_pets = int(input("Сколько питомцев вы хотите добавить?\n "))

# Заполняем словарь данными
for i in range(num_pets):
    print(f"\nВвод информации о питомце #{i+1}")
    
    pet_name = input("Введите имя питомца: ")
    
    # Создаем внутренний словарь для текущего питомца
    pet_info = {}
    
    pet_info['Вид питомца'] = input("Введите вид питомца: ")
    
    # Преобразуем возраст в int
    age = int(input("Введите возраст питомца: "))
    pet_info['Возраст питомца'] = age
    
    pet_info['Имя владельца'] = input("Введите имя владельца: ")
    
    # Добавляем информацию о питомце в основной словарь
    pets[pet_name] = pet_info
 
while True:
    print("\nЧто вы хотите сделать?")
    print("1 - Получить информацию о конкретном питомце")
    print("2 - Выйти из программы")
    
    choice = input("Введите номер выбора (1 или 2): ").strip()
    
    if choice == "1":
        # Запрашиваем имя питомца
        search_name = input("\nВведите имя питомца, о котором хотите получить информацию: ").strip()
        
        # Проверяем, есть ли такой питомец в словаре
        if search_name in pets:
            pet_info = pets[search_name]
            
            # Получаем возраст и склоняем слово "год"
            age = pet_info['Возраст питомца']
            age_suffix = get_age_suffix(age)
            
            # Формируем строку с информацией
            info_string = f'Это {pet_info["Вид питомца"].lower()} по кличке "{search_name}". '
            info_string += f'Возраст питомца: {age} {age_suffix}. '
            info_string += f'Имя владельца: {pet_info["Имя владельца"]}.'
            
            print(f"\nИнформация о питомце {search_name}:")
            print(info_string)
        else:
            print(f"\nПитомец с именем '{search_name}' не найден.")
            print("Попробуйте снова или проверьте правильность ввода.")
    
    elif choice == "2":
        print("\nВыход из программы. До свидания!")
        break
    
    else:
        print("\nНеверный ввод. Пожалуйста, введите 1 или 2.")