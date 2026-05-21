import json
import os

FILENAME = "books.json"

def load_books():
    """Загружает список книг из JSON-файла."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_books(books):
    """Сохраняет список книг в JSON-файл."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def add_book():
    """Запрашивает данные о книге у пользователя и сохраняет в файл."""
    books = load_books()
    
    print("\n--- Добавление новой книги ---")
    author = input("Введите автора книги: ").strip()
    title = input("Введите название книги: ").strip()
    

    while True:
        try:
            rating = int(input("Введите вашу оценку (от 1 до 5): "))
            if 1 <= rating <= 5:
                break
            print("Ошибка: Оценка должна быть в диапазоне от 1 до 5.")
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")
            
    date_read = input("Введите дату прочтения (например, ГГГГ-ММ-ДД): ").strip()
    
    new_book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date_read": date_read
    }
    
    books.append(new_book)
    save_books(books)
    print(f"\nУспех! Книга «{title}» сохранена.")

def main():
    while True:
        print("\n--- ТРЕКЕР ПРОЧИТАННЫХ КНИГ ---")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        
        choice = input("\nВыберите действие (1-6): ").strip()
        
        if choice == "1":
            add_book()  
        elif choice == "2":
            print("\n[В разработке] Просмотр всех книг...")
        elif choice == "3":
            print("\n[В разработке] Просмотр средней оценки...")
        elif choice == "4":
            print("\n[В разработке] Просмотр статистики по авторам...")
        elif choice == "5":
            print("\n[В разработке] Удаление книги...")
        elif choice == "6":
            print("\nВыход из программы. До свидания!")
            break
        else:
            print("\nНекорректный ввод. Пожалуйста, выберите пункт от 1 до 6.")

if __name__ == "__main__":
    main()