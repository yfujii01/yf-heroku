import os

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
    return 'xyz'
