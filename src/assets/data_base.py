import sqlite3

class PlateNum_DB:
    def __init__(self):
        self.conn = sqlite3.connect('../src/resources/num_plate_db/num_plates.db')
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS numbers(
                            data DATA PRIMARY KEY,
                            number TEXT,
                            city TEXT,
                            first_name TEXT,
                            second_name TEXT)""")

    def insert(self, item):
        self.cur.execute("""INSERT OR IGNORE INTO numbers VALUES(?,?,?,?,?)""", item)
        self.conn.commit()
        self.conn.close()

    def read_all(self):
        self.cur.execute("""SELECT * FROM numbers""")
        rows = self.cur.fetchall()
        self.conn.close()
        return rows

    def read_one(self, number):
        self.cur.execute("""SELECT * FROM numbers WHERE number=?""", (number,))
        row = self.cur.fetchone()
        self.conn.close()
        return row

    def delete_one(self, number):
        self.cur.execute("""DELETE FROM numbers WHERE number=?""", (number,))
        self.conn.commit()
        self.conn.close()

