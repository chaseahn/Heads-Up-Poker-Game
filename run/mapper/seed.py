import sqlite3
import hashlib
#from model import SALT
#from model import pass_hash
import time

def run(dbname="poker.db"):

    conn = sqlite3.connect(dbname)
    cur  = conn.cursor()

    #password = pass_hash('cookiemonster')

    SQL = """INSERT INTO computer 
        (username, pw_hash, balance, pot, win, loss) 
        VALUES (?, ?, ?, ?, ?, ?); """

    cur.execute(SQL, ('master', 'cookiemonster', 100000000000.0, 0.0, 0, 0))

    SQL = """INSERT INTO player 
        (username, player_id, pw_hash, balance, pot, win, loss) 
        VALUES (?, ?, ?, ?, ?, ?, ?); """

    cur.execute(SQL, ('player1', '000001', 'password', 0.0, 0.0, 0, 0))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    run()
