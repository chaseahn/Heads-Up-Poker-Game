from card_deck import deck,shuffle,royals,high_hands,numlist
import sqlite3
import opencursor
from opencursor import OpenCursor
import schema

opencursor.setDB('poker.db')
d = shuffle(deck)
u_hand, d_hand, burn, flop, turn, river = [], [], [], [], [], []

def deal_cards():
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

def order_hand(u_hand):
    hh2 = [t[::-1] for t in high_hands]
    if u_hand[0][0] in royals or u_hand[1][0] in royals:
        if u_hand[0][0] == 'A':
            return u_hand
        elif (u_hand[0][0],(u_hand[1][0])) in hh2:
            new_hand = [(u_hand[1][0],u_hand[1][1]),(u_hand[0][0],u_hand[0][1])]
            return new_hand
        elif u_hand[1][0] in royals and u_hand[0][0] not in royals:
            new_hand = [(u_hand[1][0],u_hand[1][1]),(u_hand[0][0],u_hand[0][1])]
            return new_hand
        else:
            return u_hand
    elif u_hand[0][0] == 'T':
        return u_hand
    elif u_hand[1][0] == 'T' and u_hand[0][0] in numlist:
        new_hand = [(u_hand[1][0],u_hand[1][1]),(u_hand[0][0],u_hand[0][1])]
        return new_hand
    elif u_hand[0][0] in numlist and u_hand[1][0] in numlist:
        if int(u_hand[1][0]) > int(u_hand[0][0]):
            new_hand = [(u_hand[1][0],u_hand[1][1]),(u_hand[0][0],u_hand[0][1])]
            return new_hand
        else:
            return u_hand
    else:
        return u_hand
        

class Computer:

    def __init__(self, row={}, username='', password=''):
        if username:
            self.check_cred(username,password)
        else:
            self.row_set({})
    
    def row_set(self,row={}):
        row           = dict(row)
        self.pk       = row.get('pk')
        self.username = row.get('username')
        self.pw_hash  = row.get('pw_hash')
        self.balance  = row.get('balance')
        self.pot      = row.get('pot')
        self.win      = row.get('win')
        self.loss     = row.get('loss')
    
    def check_cred(self,username,password):
        #pw_hash = pass_hash(password)
        with OpenCursor() as cur:
            SQL = """ SELECT * FROM computer WHERE
                  username=? and pw_hash=?; """
            val = (username,password)
            cur.execute(SQL,val)
            row = cur.fetchone()
        if row:
            self.row_set(row)
        else:
            self.row_set({})

    def __bool__(self):
        return bool(self.pk)

    def buy_in(self,amount):
        self.balance -= float(amount)
        self.pot += float(amount)
        self.save()
    
    def blind(self,amount=2):
        self.pot -= amount
        self.save()
    
    def save(self):
        with OpenCursor() as cur:
            SQL = """ UPDATE computer SET
                    username=?, pw_hash=?, balance=?, pot=?,
                    win=?, loss=?; """
            val = (self.username,self.pw_hash,self.balance,
                    self.pot, self.win,self.loss)
            cur.execute(SQL,val)

class Player:

    def __init__(self, row={}, username='', password=''):
        if username:
            self.check_cred(username,password)
        else:
            self.row_set({})

    def row_set(self,row={}):
        row            = dict(row)
        self.pk        = row.get('pk')
        self.username  = row.get('username')
        self.player_id = row.get('player_id')
        self.pw_hash   = row.get('pw_hash')
        self.balance   = row.get('balance')
        self.pot       = row.get('pot')
        self.win       = row.get('win')
        self.loss      = row.get('loss')

    def __bool__(self):
        return bool(self.pk)
    
    def check_cred(self,username,password):
        #pw_hash = pass_hash(password)
        with OpenCursor() as cur:
            SQL = """ SELECT * FROM player WHERE
                  username=? and pw_hash=?; """
            val = (username,password)
            cur.execute(SQL,val)
            row = cur.fetchone()
        if row:
            self.row_set(row)
        else:
            self.row_set({})
    
    def get_comp(self):
        with OpenCursor() as cur:
            SQL = """ SELECT * FROM computer WHERE pk = ?;"""
            cur.execute(SQL,(1,))
            row = cur.fetchone()
        return Computer(row)
    
    def deposit(self,amount):
        self.balance += float(amount)
        self.save()
    
    def blind(self,amount=2):
        self.pot -= amount
        self.save()
        
    
    def buy_in(self,amount):
        if self.balance < float(amount) or float(amount)<100:
            raise ValueError
        else:
            self.balance -= float(amount)
            self.pot += float(amount)
            self.save()


    def cash_out(self,amount):
        self.balance += float(amount)
        self.save()

    def record_player_loss(self):
        self.win += 1
        self.save()

    def record_player_loss(self):
        self.loss += 1
        self.save()
    
    def record_computer_win(self):
        comp = self.get_comp()
        comp.win += 1
        comp.save()

    def record_computer_loss(self):
        comp = self.get_comp()
        comp.loss += 1
        comp.save()

    def save(self):
        if self:
            with OpenCursor() as cur:
                SQL = """ UPDATE player SET
                      username=?, player_id=?, pw_hash=?, 
                      balance=?, pot=?, win=?, loss=?; """
                val = (self.username,self.player_id,self.pw_hash,
                       self.balance,self.pot,self.win,self.loss)
                cur.execute(SQL,val)
        else:
            with OpenCursor() as cur:
                SQL = """ INSERT INTO player (
                      username, player_id, pw_hash,
                      balance, pot, win, loss ) VALUES (
                      ?, ?, ?, ?, ?, ?, ?); """
                val = (self.username,self.player_id,self.pw_hash,
                       self.balance,self.pot,self.win,self.loss)
                cur.execute(SQL,val)
                self.pk = cur.lastrowid()
    
class Hands:

    def __init__(self, row={}, username='', password=''):
        row            = dict(row)
        self.pk        = row.get('pk')
        self.board     = row.get('username')
        self.win_hand  = row.get('player_id')
        self.loss_hand = row.get('pw_hash')
        self.win_type  = row.get('balance')

    def __bool__(self):
        return bool(self.pk)
    
    def save(self):
        with OpenCursor() as cur:
            SQL = """ INSERT INTO hands (
                    board, win_hand, loss_hand, win_type 
                    ) VALUES ( ?, ?, ?, ?, ?, ? ); """
            val = (self.board,self.win_hand,self.loss_hand,self.win_type)
            cur.execute(SQL,val)
            self.pk = cur.lastrowid()

class Hands:

    def __init__(self, row={}):
        row            = dict(row)
        self.pk        = row.get('pk')
        self.board     = row.get('username')
        self.win_hand  = row.get('win_hand')
        self.loss_hand = row.get('loss_hand')
        self.win_type  = row.get('win_type')

    def __bool__(self):
        return bool(self.pk)
    
    def save(self):
        with OpenCursor() as cur:
            SQL = """ INSERT INTO hands (
                    board, win_hand, loss_hand, win_type 
                    ) VALUES ( ?, ?, ?, ?, ?, ? ); """
            val = (self.board,self.win_hand,self.loss_hand,self.win_type)
            cur.execute(SQL,val)
            self.pk = cur.lastrowid()

class History:

    def __init__(self,row={}):
        row            = {}
        self.pk        = row.get('pk')
        self.player_pk = row.get('player_pk')
        self.amount    = row.get('amount')
        self.win_loss  = row.get('win_loss')
        self.hand_pk   = row.get('hand_pk')
    
    def __bool__(self):
        return bool(self.pk)

    def save(self):
        with OpenCursor() as cur:
            SQL = """ INSERT INTO history (
                  player_pk, amount, win_loss, hand_pk
                  ) VALUES ( ?, ?, ?, ?, ?, ? ); """
            val = (self.player_pk,self.amount,self.win_loss,self.hand_pk)
            cur.execute(SQL,val)
            self.pk = cur.lastrowid()
