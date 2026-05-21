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

def list_books():
    """Выводит список всех сохраненных книг."""
    books = load_books()
    if not books:
        print("\nВаш трекер пуст. Самое время добавить первую книгу!")
        return
        
    print("\n--- Список прочитанных книг ---")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. «{book['title']}» — {book['author']} | Оценка: {book['rating']}/5 | Дата: {book['date_read']}")

def show_average_rating():
    """Рассчитывает и выводит среднюю оценку по всем книгам."""
    books = load_books()
    if not books:
        print("\nНет данных для расчета средней оценки.")
        return
        
    total_rating = sum(book['rating'] for book in books)
    avg_rating = total_rating / len(books)
    print(f"\nСредняя оценка ваших книг: {avg_rating:.2f} из 5")

def show_author_stats():
    """Выводит количество прочитанных книг по каждому автору."""
    books = load_books()
    if not books:
        print("\nНет данных для расчета статистики.")
        return
        
    stats = {}
    for book in books:
        author = book['author']
        stats[author] = stats.get(author, 0) + 1
        
    print("\n--- Статистика по авторам ---")
    for author, count in stats.items():
        print(f"Автор: {author} — Прочитано книг: {count}")

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
            list_books()      
        elif choice == "3":
            show_average_rating() 
        elif choice == "4":
            show_author_stats()   
        elif choice == "5":
            print("\n[В разработке] Удаление книги...")
        elif choice == "6":
            print("\nВыход из программы. До свидания!")
            break
        else:
            print("\nНекорректный ввод. Пожалуйста, выберите пункт от 1 до 6.")

if __name__ == "__main__":
    main()
