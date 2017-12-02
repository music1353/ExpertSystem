# coding: utf-8

# 專家系統問答

import sys
sys.path.append('expertEngine')
from expertEngine import herbologySystem as hs

path = 'knowledgeBase.json' # database路徑
eS = hs.expertSystem(path)

eS.run()