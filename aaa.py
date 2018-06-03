import os
import psycopg2
from psycopg2.extras import DictCursor

from os.path import join, dirname
from dotenv import load_dotenv

"""
環境設定ファイル(.env)の読み込み
ローカル環境のみ
"""
dotenv_path = join(dirname(__file__), '.env')
print(dotenv_path)

if os.path.exists(dotenv_path):
    print('yes')
    load_dotenv(dotenv_path)
else:
    print('else')


def exe():
    print('hello')

    print(get_param())

    return 'xyz'


def get_connection():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    return conn


def get_param():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=DictCursor)
    cur.execute('SELECT * FROM t_param')
    result = cur.fetchall()

    cur.close()
    conn.close()

    return result
