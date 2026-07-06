from db.crud import get_all_categories, get_all_books, get_books_by_category
from db.db import get_db_connection

def display_categories_and_books():
    """Выводит все категории и книги на экран"""
    
    print("\n" + "=" * 60)
    print("КАТАЛОГ КНИГ")
    print("=" * 60)
    
    # Получаем все категории
    categories = get_all_categories()
    
    if not categories:
        print("\nВ базе данных нет категорий.")
        print("Запустите сначала app/db/init_db.py для заполнения БД.")
        return
    
    print(f"\nВсего категорий: {len(categories)}\n")
    
    # Для каждой категории выводим книги
    for category in categories:
        cat_id = category[0]
        cat_title = category[1]
        
        print(f"\n📚 КАТЕГОРИЯ: {cat_title.upper()} (ID: {cat_id})")
        print("-" * 60)
        
        # Получаем книги для этой категории
        books = get_books_by_category(cat_id)
        
        if not books:
            print("  В этой категории пока нет книг.")
        else:
            print(f"  Всего книг: {len(books)}\n")
            for book in books:
                book_id = book[0]
                title = book[1]
                description = book[2]
                price = book[3]
                url = book[4]
                
                print(f"  📖 {title}")
                print(f"     ID: {book_id}")
                if len(description) > 80:
                    print(f"     Описание: {description[:80]}...")
                else:
                    print(f"     Описание: {description}")
                print(f"     Цена: {price} ₽")
                print(f"     Ссылка: {url}")
                print()
    
    print("=" * 60)
    
    # Дополнительная статистика
    all_books = get_all_books()
    total_books = len(all_books)
    total_categories = len(categories)
    
    print(f"\n📊 СТАТИСТИКА:")
    print(f"  - Всего книг в базе: {total_books}")
    print(f"  - Всего категорий: {total_categories}")
    
    # Вычисляем среднюю цену
    if all_books:
        total_price = sum(book[3] for book in all_books)
        avg_price = total_price / total_books
        print(f"  - Средняя цена книги: {avg_price:.2f} ₽")
        print(f"  - Самая дорогая книга: {max(book[3] for book in all_books):.2f} ₽")
        print(f"  - Самая дешевая книга: {min(book[3] for book in all_books):.2f} ₽")
    
    print("\n" + "=" * 60)

def main():
    """Главная функция"""
    # Проверяем подключение к БД
    conn = get_db_connection()
    if not conn:
        print("Ошибка: Не удалось подключиться к базе данных.")
        print("Проверьте настройки в .env файле.")
        return
    conn.close()
    
    # Выводим данные
    display_categories_and_books()

if __name__ == "__main__":
    main()