import sqlite3

table1 = "table1"
table2 = "table2"

def new_user(name:str, last_name:str, tg_id:int, username:str, phone:str, city:str):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    
    cursor.execute(f"""INSERT INTO {table1}
                        VALUES ("{name}", "{last_name}", "{tg_id}", "{username}", "{phone}", "{city}", "0", "member", "true")
                   """
                   )
    
    conn.commit()

def check_profile(tg_id:int) -> dict:
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM {table1}
                        WHERE telegram_id IN ({tg_id})
                   """
                   )
    
    desc = cursor.description
    column_names = [col[0] for col in desc]
    record = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    return record

def change_user_info(t_id:int, type:str, new:str):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""UPDATE {table1} 
                   SET {type} = "{new}" 
                   WHERE telegram_id = {t_id}""")
    
    conn.commit()


def clear():
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""DELETE FROM {table1}""")
    conn.commit()

def new_order(tg_id: int, track_num: str, status: str):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    
    cursor.execute(f"""INSERT INTO {table2}
                        VALUES ("{tg_id}", "{track_num}", "{status}", NULL)
                   """
                   )
    
    conn.commit()

def people_orders(tg_id: int) -> dict:
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    
    cursor.execute(f"""SELECT * FROM {table2}
                        WHERE telegram_id IN ({tg_id})
                   """
                   )
    
    desc = cursor.description
    column_names = [col[0] for col in desc]
    rows = cursor.fetchall()
    if rows:
        record = [dict(zip(column_names, row)) for row in rows]

    else:
        record = dict()

    return record

def check_order_id(order_id: int) -> dict:
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM {table2}
                        WHERE id IN ({order_id})
                   """
                   )
    
    desc = cursor.description
    column_names = [col[0] for col in desc]
    record = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    return record

def check_order_track_num(track_num: str) -> dict:
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM {table2}
                        WHERE track_num = "{track_num}"
                   """
                   )
    
    desc = cursor.description
    column_names = [col[0] for col in desc]
    record = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    return record

def change_order_info(track_num:str, type:str, new:str):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""UPDATE {table2} 
                   SET {type} = "{new}" 
                   WHERE track_num = "{track_num}"
                   """)
    
    conn.commit()

def check_customers_id(track_num: str) -> list:
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT telegram_id, id FROM {table2}
                        WHERE track_num = "{track_num}"
                   """
                   )
    
    desc = cursor.description
    column_names = [col[0] for col in desc]
    record = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    return record

def clear_order():
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()

    cursor.execute(f"""DELETE FROM {table2}""")
    conn.commit()