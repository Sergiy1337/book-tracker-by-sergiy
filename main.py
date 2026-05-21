import json
import os

FILENAME = "books.json"

def load_books():
    """Эта функция читает книги из файла books.json."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_books(books):
    """Эта функция записывает изменения в файл books.json."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def main():
    """Главный цикл программы, который показывает меню."""
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
            print("\n[В разработке] Добавление книги...")
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