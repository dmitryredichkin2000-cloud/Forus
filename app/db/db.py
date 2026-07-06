# app/db/db.py
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Параметры подключения к БД из переменных окружения
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'your_database_name'),
    'user': os.getenv('DB_USER', 'octagon'),
    'password': os.getenv('DB_PASSWORD', '12345'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432')
}

def get_db_connection():
    """Создает и возвращает подключение к БД"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Ошибка подключения к БД: {e}")
        return None

def close_db_connection(conn):
    """Закрывает подключение к БД"""
    if conn:
        conn.close()