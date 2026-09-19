# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:33:39 2026

@author: green
"""

import sqlite3 as sq

def get_connection():
    return sq.Connection('gambling_database_full.db')

def insert_player(NA_id, name):
    conn=get_connection()
    cur=conn.cursor()
    try:
        cur.execute(''' SELECT name FROM player WHERE NA_id = ? ''',(NA_id,))
        player = cur.fetchone()
        if player is not None:
            if player[0] == name :
                return 'existing'
            return 'diffrent_name'
        cur.execute(''' INSERT INTO player(NA_id, name) VALUES (?, ?)''',(NA_id, name))
        conn.commit()
        return 'new'
    finally:
        conn.close()

def insert_game(NA_id, attempts):
    conn=get_connection()
    cur=conn.cursor()
    try:
        cur.execute(''' INSERT INTO games(NA_id, attempts) VALUES (?, ?)''',(NA_id, attempts)) 
        conn.commit()
    except sq.IntegrityError :
        conn.rollback()
        raise
    finally:
        conn.close()
        
def get_player(NA_id):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute(''' SELECT NA_id, name FROM  player WHERE NA_id= ? ''', (NA_id,))
    player = cur.fetchone()
    conn.close()
    return player

def get_games(NA_id):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute(''' SELECT game_id, NA_id, attempts, played_at FROM  games WHERE NA_id= ? ''', (NA_id,))
    games = cur.fetchall()
    conn.close()
    return games

def get_best_attempts(NA_id):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute(''' SELECT MIN(attempts) FROM  games WHERE NA_id= ? ''', (NA_id,))
    best_score = cur.fetchone()
    conn.close()
    return best_score[0]

def get_top_three_players():
    conn=get_connection()
    cur=conn.cursor()
    cur.execute(''' SELECT player.name, MIN(games.attempts) FROM player JOIN games ON player.NA_id 
                = games.NA_id GROUP BY player.NA_id, player.name ORDER BY MIN(games.attempts) ASC LIMIT 3 ''' )
    top_players = cur.fetchall()
    conn.close()
    return top_players


    
    
        
        
        

























conn=get_connection()

conn.close()