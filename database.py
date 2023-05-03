import sqlite3

DB_NAME = "event_city_bot.db"


def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                      user_id INTEGER PRIMARY KEY,
                      city TEXT
                      )""")

    conn.commit()
    conn.close()


def set_user_city(user_id: int, city: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("INSERT OR REPLACE INTO users (user_id, city) VALUES (?, ?)", (user_id, city))

    conn.commit()
    conn.close()


def get_user_city(user_id: int) -> str:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT city FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return None

async def close_db():
    if pool:
        await pool.close()

if __name__ == "__main__":
    create_tables()
