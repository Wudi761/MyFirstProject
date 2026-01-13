
import collections

pets ={}

# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==========

def get_pet(ID):
    """Получение информации о питомце по ID"""
    return pets[ID] if ID in pets else False

def get_suffix(age):
    """Получение правильного склонения слова 'год' для возраста"""
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

def pets_list():
    """Отображение списка всех питомцев"""
    if not pets:
        print("База данных питомцев пуста.")
        return
    
    print("\n=== СПИСОК ВСЕХ ПИТОМЦЕВ ===")
    for pet_id, pet_info in pets.items():
        pet_name = list(pet_info.keys())[0]
        pet_data = pet_info[pet_name]
        age = pet_data["Возраст питомца"]
        suffix = get_suffix(age)
        
        print(f"ID: {pet_id}")
        print(f"  Кличка: {pet_name}")
        print(f"  Вид: {pet_data['Вид питомца']}")
        print(f"  Возраст: {age} {suffix}")
        print(f"  Владелец: {pet_data['Имя владельца']}")
        print("-" * 30)

# ========== ОСНОВНЫЕ ФУНКЦИИ CRUD ==========

def create():
    """Создание новой записи о питомце"""
    print("\n=== ДОБАВЛЕНИЕ НОВОГО ПИТОМЦА ===")
    
    # Получаем следующий ID
    last_id = 0
    if pets:  # если словарь не пустой
        last_id = collections.deque(pets, maxlen=1)[0]
    new_id = last_id + 1
    
    # Ввод данных
    name = input("Введите кличку питомца: ").strip()
    if not name:
        print("Ошибка: кличка не может быть пустой!")
        return
    
    species = input("Введите вид питомца: ").strip()
    if not species:
        print("Ошибка: вид питомца не может быть пустым!")
        return
    
    # Проверка возраста
    try:
        age = int(input("Введите возраст питомца: ").strip())
        if age < 0:
            print("Ошибка: возраст не может быть отрицательным!")
            return
    except ValueError:
        print("Ошибка: возраст должен быть числом!")
        return
    
    owner = input("Введите имя владельца: ").strip()
    if not owner:
        print("Ошибка: имя владельца не может быть пустым!")
        return
    
    # Добавляем в базу данных
    pets[new_id] = {
        name: {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    
    print(f"Питомец успешно добавлен с ID: {new_id}")

def read():
    """Чтение информации о питомце по ID"""
    print("\n=== ПРОСМОТР ИНФОРМАЦИИ О ПИТОМЦЕ ===")
    
    try:
        pet_id = int(input("Введите ID питомца: ").strip())
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return
    
    pet_info = get_pet(pet_id)
    
    if not pet_info:
        print(f"Питомец с ID {pet_id} не найден.")
        return
    
    # Извлекаем данные
    pet_name = list(pet_info.keys())[0]
    pet_data = pet_info[pet_name]
    species = pet_data["Вид питомца"]
    age = pet_data["Возраст питомца"]
    owner = pet_data["Имя владельца"]
    suffix = get_suffix(age)
    
    # Форматированный вывод
    print(f'\nЭто {species.lower()} по кличке "{pet_name}". '
          f'Возраст питомца: {age} {suffix}. '
          f'Имя владельца: {owner}')

def update():
    """Обновление информации о питомце"""
    print("\n=== ОБНОВЛЕНИЕ ИНФОРМАЦИИ О ПИТОМЦЕ ===")
    
    try:
        pet_id = int(input("Введите ID питомца для обновления: ").strip())
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return
    
    pet_info = get_pet(pet_id)
    
    if not pet_info:
        print(f"Питомец с ID {pet_id} не найден.")
        return
    
    pet_name = list(pet_info.keys())[0]
    pet_data = pet_info[pet_name]
    
    print(f"Текущая информация о питомце {pet_name}:")
    print(f"1. Вид питомца: {pet_data['Вид питомца']}")
    print(f"2. Возраст питомца: {pet_data['Возраст питомца']}")
    print(f"3. Имя владельца: {pet_data['Имя владельца']}")
    
    print("\nВведите новые данные (оставьте пустым, чтобы не менять):")
    
    # Обновление вида питомца
    new_species = input(f"Вид питомца [{pet_data['Вид питомца']}]: ").strip()
    if new_species:
        pet_data["Вид питомца"] = new_species
    
    # Обновление возраста
    new_age = input(f"Возраст питомца [{pet_data['Возраст питомца']}]: ").strip()
    if new_age:
        try:
            age = int(new_age)
            if age < 0:
                print("Ошибка: возраст не может быть отрицательным!")
                return
            pet_data["Возраст питомца"] = age
        except ValueError:
            print("Ошибка: возраст должен быть числом!")
            return
    
    # Обновление имени владельца
    new_owner = input(f"Имя владельца [{pet_data['Имя владельца']}]: ").strip()
    if new_owner:
        pet_data["Имя владельца"] = new_owner
    
    print(f"Информация о питомце {pet_name} успешно обновлена!")

def delete():
    """Удаление записи о питомце"""
    print("\n=== УДАЛЕНИЕ ПИТОМЦА ===")
    
    try:
        pet_id = int(input("Введите ID питомца для удаления: ").strip())
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return
    
    pet_info = get_pet(pet_id)
    
    if not pet_info:
        print(f"Питомец с ID {pet_id} не найден.")
        return
    
    pet_name = list(pet_info.keys())[0]
    
    # Подтверждение удаления
    confirm = input(f"Вы уверены, что хотите удалить питомца {pet_name}? (да/нет): ").strip().lower()
    
    if confirm == 'да':
        del pets[pet_id]
        print(f"Питомец {pet_name} (ID: {pet_id}) успешно удален!")
    else:
        print("Удаление отменено.")

# ========== ОСНОВНАЯ ПРОГРАММА ==========

def main():
    """Основная функция программы"""
    print("=== ПРОГРАММА УЧЕТА ПИТОМЦЕВ ===")
    print("Доступные команды:")
    print("  create - добавить нового питомца")
    print("  read   - просмотреть информацию о питомце")
    print("  update - обновить информацию о питомце")
    print("  delete - удалить питомца")
    print("  list   - показать всех питомцев")
    print("  stop   - завершить программу")
    
    command = ""
    
    while command != 'stop':
        print("\n" + "="*40)
        command = input("Введите команду: ").strip().lower()
        
        if command == 'create':
            create()
        elif command == 'read':
            read()
        elif command == 'update':
            update()
        elif command == 'delete':
            delete()
        elif command == 'list':
            pets_list()
        elif command == 'stop':
            print("Программа завершена. До свидания!")
        elif command == 'help':
            print("Доступные команды:")
            print("  create - добавить нового питомца")
            print("  read   - просмотреть информацию о питомце")
            print("  update - обновить информацию о питомце")
            print("  delete - удалить питомца")
            print("  list   - показать всех питомцев")
            print("  stop   - завершить программу")
            print("  help   - показать список команд")
        else:
            print(f"Неизвестная команда: '{command}'")
            print("Введите 'help' для просмотра доступных команд")

# Запуск программы
if __name__ == "__main__":
    main()