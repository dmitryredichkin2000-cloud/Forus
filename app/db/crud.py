from sqlalchemy.orm import Session

from app.db.models import Book, Category

# ==========================================================
# CRUD для таблицы categories
# ==========================================================

def create_category(db: Session, title: str):
    """
    Создание новой категории.
    """
    category = Category(title=title)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category

def get_category(db: Session, category_id: int):
    """
    Получение категории по ID.
    """
    return (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )

def get_all_categories(db: Session):
    """
    Получение всех категорий.
    """
    return (
        db.query(Category)
        .order_by(Category.id)
        .all()
    )

def update_category(db: Session, category_id: int, new_title: str):
    """
    Обновление категории.
    """
    category = get_category(db, category_id)

    if category is None:
        return None

    category.title = new_title

    db.commit()
    db.refresh(category)

    return category

def delete_category(db: Session, category_id: int):
    """
    Удаление категории.
    """
    category = get_category(db, category_id)

    if category is None:
        return None

    db.delete(category)
    db.commit()

    return category

# ==========================================================
# CRUD для таблицы books
# ==========================================================

def create_book(
    db: Session,
    title: str,
    description: str,
    price: float,
    category_id: int,
    url: str = ""
):
    """
    Создание новой книги.
    """
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book

def get_book(db: Session, book_id: int):
    """
    Получение книги по ID.
    """
    return (
        db.query(Book)
        .filter(Book.id == book_id)
        .first()
    )

def get_all_books(db: Session):
    """
    Получение всех книг.
    """
    return (
        db.query(Book)
        .order_by(Book.id)
        .all()
    )

def get_books_by_category(db: Session, category_id: int):
    """
    Получение книг по категории.
    """
    return (
        db.query(Book)
        .filter(Book.category_id == category_id)
        .order_by(Book.id)
        .all()
    )

def update_book(
    db: Session,
    book_id: int,
    title: str | None = None,
    description: str | None = None,
    price: float | None = None,
    url: str | None = None,
    category_id: int | None = None
):
    """
    Обновление книги.
    Можно обновлять как все поля, так и отдельные.
    """
    book = get_book(db, book_id)

    if book is None:
        return None

    if title is not None:
        book.title = title

    if description is not None:
        book.description = description

    if price is not None:
        book.price = price

    if url is not None:
        book.url = url

    if category_id is not None:
        book.category_id = category_id

    db.commit()
    db.refresh(book)

    return book

def delete_book(db: Session, book_id: int):
    """
    Удаление книги.
    """
    book = get_book(db, book_id)

    if book is None:
        return None

    db.delete(book)
    db.commit()

    return book