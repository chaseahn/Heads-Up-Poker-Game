from card_deck import deck,shuffle

d = shuffle(deck)
u_hand, d_hand, burn, flop, turn, river = [], [], [], [], [], []

def deal_cards():
    print(d)
    u1,d1,u2,d2,b1,f1,f2,f3,b2,t1,b3,r1 = d.pop(0),d.pop(0),d.pop(0),d.pop(0),d.pop(0),d.pop(0),d.pop(0),d.pop(0),d.pop(0),d.pop(0),d.pop(0),d.pop(0)
    u_hand.append(u1)
    d_hand.append(d1)
    u_hand.append(u2)
    d_hand.append(d2)
    burn.append(b1)
    burn.append(b2)
    burn.append(b3)
    flop.append(f1)
    flop.append(f2)
    flop.append(f3)
    turn.append(t1)
    river.append(r1)

class Computer:

    def __init__(self, row={}, username='', password=''):
        row           = dict(row)
        self.pk       = row.get('pk')
        self.username = row.get('username')
        self.pw_hash  = row.get('pw_hash')
        self.balance  = row.get('balance')
        self.win      = row.get('win')
        self.loss     = row.get('loss')

    def __bool__(self):
        return bool(self.pk)
    
    def save():
        if self:
            with OpenCursor() as cur:
                SQL = """ UPDATE computer SET
                      username=?, pw_hash=?, balance=?,
                      win=?, loss=?; """
                val = (self.username,self.pw_hash,self.balance,
                       self.win,self.loss)
                cur.execute(SQL,val)

class Player:

    def __init__(self, row={}, username='', password=''):
        row            = dict(row)
        self.pk        = row.get('pk')
        self.username  = row.get('username')
        self.player_id = row.get('player_id')
        self.pw_hash   = row.get('pw_hash')
        self.balance   = row.get('balance')
        self.win       = row.get('win')
        self.loss      = row.get('loss')

    def __bool__(self):
        return bool(self.pk)
    
    def save():
        if self:
            with OpenCursor() as cur:
                SQL = """ UPDATE computer SET
                      username=?, player_id=?, pw_hash=?, 
                      balance=?, win=?, loss=?; """
                val = (self.username,self.player_id,self.pw_hash,
                       self.balance,self.win,self.loss)
                cur.execute(SQL,val)
        else:
            with OpenCursor() as cur:
                SQL = """ INSERT INTO player (
                      username, player_id, pw_hash,
                      balance, win, loss ) VALUES (
                      ?, ?, ?, ?, ?, ? ); """
                val = (self.username,self.player_id,self.pw_hash,
                       self.balance,self.win,self.loss)
                cur.execute(SQL,val)
                self.pk = cur.lastrowid()
    


