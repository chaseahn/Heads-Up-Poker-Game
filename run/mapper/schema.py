import sqlite3

def run(dbname='poker.db'):

    CON = sqlite3.connect(dbname)
    CUR = CON.cursor()

    CUR.execute("""DROP TABLE IF EXISTS computer;""")
    # create accounts table
    CUR.execute("""CREATE TABLE computer(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR,
        pw_hash VARCHAR,
        balance INTEGER,
        pot INTEGER,
        win VARCHAR,
        loss VARCHAR
        ); """
    )

    CUR.execute("""DROP TABLE IF EXISTS player;""")
    # create accounts table
    CUR.execute("""CREATE TABLE player(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR,
        player_id VARCHAR,
        pw_hash,
        balance INTEGER,
        pot INTEGER,
        win VARCHAR,
        loss VARCHAR
        ); """
    )

    CUR.execute("""DROP TABLE IF EXISTS hands;""")
    # create accounts table
    CUR.execute("""CREATE TABLE hands(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        board VARCHAR,
        win_hand VARCHAR,
        loss_hand VARCHAR,
        win_type VARCHAR
        ); """
    )


    CUR.execute("""DROP TABLE IF EXISTS history;""")
    # create accounts table
    CUR.execute("""CREATE TABLE history(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        player_pk INTEGER,
        amount INTEGER,
        win_loss VARCHAR,
        hand_pk INTEGER,
        FOREIGN KEY(player_pk) REFERENCES player(pk),
        FOREIGN KEY(hand_pk) REFERENCES hands(pk)
        ); """
    )

    CON.commit()
    CUR.close()
    CON.close()

if __name__ == '__main__':
    run()
