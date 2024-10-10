import re


# Функція для сортування слів за правилами (українські -> латинські, незалежно від регістру)
def custom_sort(words):
    # Розділяємо слова на українські та латинські
    ukr_letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    lat_letters = 'abcdefghijklmnopqrstuvwxyz'

    def sorting_key(word):
        word_lower = word.lower()
        # Якщо перша літера українська, сортуємо за українським алфавітом
        if word_lower[0] in ukr_letters:
            return (0, word_lower)
        # Якщо латинська - за латинським
        elif word_lower[0] in lat_letters:
            return (1, word_lower)
        else:
            return (2, word_lower)

    return sorted(words, key=sorting_key)


# Функція для зчитування першого речення
def read_first_sentence(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Знаходимо перше речення
    first_sentence = re.split(r'(?<=[.!?])\s', text)[0]
    return first_sentence


# Функція для видалення пунктуації з тексту
def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)


# Основна функція
def process_text(filename):
    # Читання першого речення з файлу
    first_sentence = read_first_sentence(filename)
    print(f"Перше речення:\n{first_sentence}\n")

    # Видаляємо пунктуацію та розбиваємо текст на слова
    cleaned_text = remove_punctuation(first_sentence)
    words = cleaned_text.split()

    # Сортуємо слова за спеціальними правилами
    sorted_words = custom_sort(words)

    # Виводимо відсортовані слова та їх кількість
    print("Відсортовані слова:", sorted_words)
    print(f"Кількість слів: {len(sorted_words)}")


# Виклик основної функції
filename = 'text.txt'  # Вказуємо назву вашого файлу
process_text(filename)
