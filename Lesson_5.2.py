# Получаем слово от пользователя
word = input("Введите слово из маленьких латинских букв: ").lower()

# Определяем гласные буквы
vowels = "aeiou"
vowels_count = 0

# Создаем словарь для подсчета каждой гласной буквы
vowel_counts = {vowel: 0 for vowel in vowels}

# Перебираем буквы в слове
for letter in word:
    if letter in vowels:
        vowels_count += 1
        vowel_counts[letter] += 1

# Выводим количество каждой гласной буквы
print("\nКоличество каждой гласной буквы:")
for vowel in vowels:
    count = vowel_counts[vowel]
    if count > 0:
        print(f"  {vowel}: {count}")
    else:
        print(f"  {vowel}: False")
