# coding: utf-8

# 查看dababase的資料

import sys
sys.path.append('expertEngine')
from expertEngine import herbologySystem as hs

path = 'knowledgeBase.json' # database路徑
expertSystem = hs.expertSystem(path) # 啟動expertEngin

expertSystem.list_database() # 列出知識庫資料