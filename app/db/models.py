from .db import get_db_connection

def create_tables():
    """Создает таблицы categories и books, если их нет"""
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        cur = conn.cursor()
        
        # Создание таблицы categories
        cur.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL UNIQUE
            )
        """)
        
        # Создание таблицы books
        cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                price DECIMAL(10, 2) NOT NULL,
                url VARCHAR(500) DEFAULT '',
                category_id INTEGER REFERENCES categories(id) ON DELETE CASCADE
            )
        """)
        
        conn.commit()
        cur.close()
        print("Таблицы успешно созданы (или уже существуют)")
        return True
        
    except Exception as e:
        print(f"Ошибка создания таблиц: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()