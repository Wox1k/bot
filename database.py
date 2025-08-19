import sqlite3

table_name = "table1"

def new_user(name:str, last_name:str, tg_id:int, username:str, phone:str, city:str):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    
    cursor.execute(f"""INSERT INTO {table_name}
                        VALUES ("{name}", "{last_name}", "{tg_id}", "{username}", "{phone}", "{city}")
                   """
                   )
    
    conn.commit()

def check_profile(tg_id:int) -> list:
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM {table_name}
                        WHERE telegram_id IN ({tg_id})
                   """
                   )
    
    record = cursor.fetchone()

    if record:
        return list(record)
    
    return []

def change_user_info(t_id:int, type:str, new:str):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""UPDATE {table_name} 
                   SET {type} = "{new}" 
                   WHERE telegram_id = {t_id}""")
    
    conn.commit()


def clear():
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""DELETE FROM {table_name}""")
    conn.commit()