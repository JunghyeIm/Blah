import sqlite3
from sqlite3 import Error

try:
    con = sqlite3.connect(':memory:')
    print("DB created in memory")
except Error:
    print(Error)
finally:
    con.close()

# db 생성
def connection():
    try:
        con = sqlite3.connect('test.db')
        return con
    except Error:
        print(Error)

# 테이블 생성
def create_table(con):
    cursor_db = con.cursor()
    cursor_db.execute("CREATE TABLE ingredients (cosmetic, ingredient)")
    con.commit()

con = connection()
#create_table(con)

# 테이블 조회
