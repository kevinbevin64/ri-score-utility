import sqlite3



def initialize_table(table_name):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    
    with conn:
        c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
        exam_name text,    
        weightage real,
        score_attained real,
        score_max real
        )""")
    with conn:
        c.execute(f"INSERT INTO {table_name} VALUES ('wa1', 0, 0, 0)")
        c.execute(f"INSERT INTO {table_name} VALUES ('wa2', 0, 0, 0)")
        c.execute(f"INSERT INTO {table_name} VALUES ('wa3', 0, 0, 0)")
        c.execute(f"INSERT INTO {table_name} VALUES ('eoy', 0, 0, 0)")
    

def update_values(table_name, exam_name, weightage, score_attained, score_max):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    
    with conn:
        c.execute(f"UPDATE {table_name} SET weightage={weightage} WHERE exam_name='{exam_name}'")
        c.execute(f"UPDATE {table_name} SET score_attained={score_attained} WHERE exam_name='{exam_name}'")
        c.execute(f"UPDATE {table_name} SET score_max={score_max} WHERE exam_name='{exam_name}'")


def get_stored_values(table_name):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()

    c.execute(f"SELECT * FROM {table_name}")
    return c.fetchall()
