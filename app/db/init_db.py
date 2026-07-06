from .crud import create_category, create_book, get_all_categories, get_all_books
from .models import create_tables

def init_database():
    """Создает таблицы и добавляет тестовые данные"""
    
    print("=" * 50)
    print("ИНИЦИАЛИЗАЦИЯ БАЗЫ ДАННЫХ")
    print("=" * 50)
    
    # Создаем таблицы
    print("\n1. Создание таблиц...")
    create_tables()
    
    # Проверяем, есть ли уже категории
    existing_categories = get_all_categories()
    if existing_categories:
        print("\nВ базе уже есть данные. Пропускаем добавление.")
        print(f"Найдено категорий: {len(existing_categories)}")
        return
    
    print("\n2. Добавление категорий...")
    
    # Добавляем категории (ровно 2 категории)
    cat1 = create_category("Художественная литература")
    cat2 = create_category("Научно-популярная литература")
    
    print(f"   - Создана категория: Художественная литература (ID: {cat1})")
    print(f"   - Создана категория: Научно-популярная литература (ID: {cat2})")
    
    print("\n3. Добавление книг...")
    
    # Добавляем книги в категорию "Художественная литература" (4 книги)
    if cat1:
        book1 = create_book(
            "Война и мир",
            "Роман-эпопея Льва Толстого о жизни русского общества в эпоху наполеоновских войн",
            599.99,
            cat1,
            "https://example.com/war_and_peace"
        )
        print(f"   - Добавлена книга: Война и мир (ID: {book1})")
        
        book2 = create_book(
            "Преступление и наказание",
            "Роман Федора Достоевского о моральных дилеммах и искуплении",
            450.00,
            cat1,
            "https://example.com/crime_and_punishment"
        )
        print(f"   - Добавлена книга: Преступление и наказание (ID: {book2})")
        
        book3 = create_book(
            "Мастер и Маргарита",
            "Мистический роман Михаила Булгакова о дьяволе в Москве",
            520.00,
            cat1,
            "https://example.com/master_and_margarita"
        )
        print(f"   - Добавлена книга: Мастер и Маргарита (ID: {book3})")
        
        book4 = create_book(
            "Анна Каренина",
            "Трагическая история любви в романе Льва Толстого",
            480.00,
            cat1,
            "https://example.com/anna_karenina"
        )
        print(f"   - Добавлена книга: Анна Каренина (ID: {book4})")
    
    # Добавляем книги в категорию "Научно-популярная литература" (3 книги)
    if cat2:
        book5 = create_book(
            "Краткая история времени",
            "Стивен Хокинг о происхождении Вселенной и черных дырах",
            750.00,
            cat2,
            "https://example.com/brief_history_of_time"
        )
        print(f"   - Добавлена книга: Краткая история времени (ID: {book5})")
        
        book6 = create_book(
            "Эгоистичный ген",
            "Ричард Докинз о механизмах эволюции с точки зрения генов",
            680.00,
            cat2,
            "https://example.com/selfish_gene"
        )
        print(f"   - Добавлена книга: Эгоистичный ген (ID: {book6})")
        
        book7 = create_book(
            "Sapiens. Краткая история человечества",
            "Юваль Ной Харари о ключевых этапах развития человечества",
            890.00,
            cat2,
            "https://example.com/sapiens"
        )
        print(f"   - Добавлена книга: Sapiens. Краткая история человечества (ID: {book7})")
    
    print("\n" + "=" * 50)
    print("ИНИЦИАЛИЗАЦИЯ ЗАВЕРШЕНА УСПЕШНО!")
    print("=" * 50)
    
    # Выводим итоговую статистику
    categories = get_all_categories()
    books = get_all_books()
    print(f"\nИтог:")
    print(f"  - Всего категорий: {len(categories)}")
    print(f"  - Всего книг: {len(books)}")

if __name__ == "__main__":
    init_database()