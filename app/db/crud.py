from .db import get_db_connection

def create_category(title):
    """Создание новой категории"""
    conn = get_db_connection()
    if not conn:
        return None
    
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO categories (title) VALUES (%s) RETURNING id",
            (title,)
        )
        category_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return category_id
    except Exception as e:
        print(f"Ошибка создания категории: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()

def get_category(category_id):
    """Получение категории по ID"""
    conn = get_db_connection()
    if not conn:
        return None
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, title FROM categories WHERE id = %s", (category_id,))
        category = cur.fetchone()
        cur.close()
        return category
    except Exception as e:
        print(f"Ошибка получения категории: {e}")
        return None
    finally:
        conn.close()

def get_all_categories():
    """Получение всех категорий"""
    conn = get_db_connection()
    if not conn:
        return []
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, title FROM categories ORDER BY id")
        categories = cur.fetchall()
        cur.close()
        return categories
    except Exception as e:
        print(f"Ошибка получения категорий: {e}")
        return []
    finally:
        conn.close()

def update_category(category_id, new_title):
    """Обновление категории"""
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE categories SET title = %s WHERE id = %s",
            (new_title, category_id)
        )
        conn.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Ошибка обновления категории: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_category(category_id):
    """Удаление категории"""
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM categories WHERE id = %s", (category_id,))
        conn.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Ошибка удаления категории: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# ============ CRUD для таблицы books ============

def create_book(title, description, price, category_id, url=''):
    """Создание новой книги"""
    conn = get_db_connection()
    if not conn:
        return None
    
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO books (title, description, price, url, category_id) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (title, description, price, url, category_id)
        )
        book_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return book_id
    except Exception as e:
        print(f"Ошибка создания книги: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()

def get_book(book_id):
    """Получение книги по ID"""
    conn = get_db_connection()
    if not conn:
        return None
    
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT b.id, b.title, b.description, b.price, b.url, 
                   c.id as category_id, c.title as category_title
            FROM books b
            LEFT JOIN categories c ON b.category_id = c.id
            WHERE b.id = %s
        """, (book_id,))
        book = cur.fetchone()
        cur.close()
        return book
    except Exception as e:
        print(f"Ошибка получения книги: {e}")
        return None
    finally:
        conn.close()

def get_all_books():
    """Получение всех книг"""
    conn = get_db_connection()
    if not conn:
        return []
    
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT b.id, b.title, b.description, b.price, b.url, 
                   c.id as category_id, c.title as category_title
            FROM books b
            LEFT JOIN categories c ON b.category_id = c.id
            ORDER BY b.id
        """)
        books = cur.fetchall()
        cur.close()
        return books
    except Exception as e:
        print(f"Ошибка получения книг: {e}")
        return []
    finally:
        conn.close()

def get_books_by_category(category_id):
    """Получение книг по категории"""
    conn = get_db_connection()
    if not conn:
        return []
    
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, title, description, price, url
            FROM books
            WHERE category_id = %s
            ORDER BY id
        """, (category_id,))
        books = cur.fetchall()
        cur.close()
        return books
    except Exception as e:
        print(f"Ошибка получения книг по категории: {e}")
        return []
    finally:
        conn.close()

def update_book(book_id, title=None, description=None, price=None, url=None, category_id=None):
    """Обновление книги (можно обновить отдельные поля)"""
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        cur = conn.cursor()
        
        update_fields = []
        params = []
        
        if title is not None:
            update_fields.append("title = %s")
            params.append(title)
        if description is not None:
            update_fields.append("description = %s")
            params.append(description)
        if price is not None:
            update_fields.append("price = %s")
            params.append(price)
        if url is not None:
            update_fields.append("url = %s")
            params.append(url)
        if category_id is not None:
            update_fields.append("category_id = %s")
            params.append(category_id)
        
        if not update_fields:
            return True
        
        params.append(book_id)
        query = f"UPDATE books SET {', '.join(update_fields)} WHERE id = %s"
        
        cur.execute(query, params)
        conn.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Ошибка обновления книги: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_book(book_id):
    """Удаление книги"""
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
        conn.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Ошибка удаления книги: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()