# coding: utf-8

# 專家系統問答

import sys
sys.path.append('expertEngine')
from expertEngine import herbologySystem as hs

path = 'knowledgeBase.json' # database路徑
identify = input('請問您的身份是(person/doctor)：')
    
if(identify == 'person'):
    person = hs.person(path) # 啟動person模式
    
    person.list_database_symptom()
    symptom = input('請問您的症狀是：')
    
    predict = person.match(symptom) # 比對資料庫
        
    if( predict==[] ): # 如果match不到
        print('沒有這種中藥材呦')
    elif( len(predict)==1 ): # 如果只有一種中藥材
        print('您可能需要', predict, '中藥材')
    else: # 如果不止一種，進入問答程序
        person.re_callback(predict, symptom)
            
elif(identify == 'doctor'):
    doctor = hs.doctor(path) # 啟動doctor模式
        
    intent = input('請問要新增中藥材(0), 還是刪除中藥材(1)：')
        
    if int(intent)==0:
        medicine = input('請問要新增的中藥材是：')
        symptom = input('適用症狀為：')
        doctor.add_knowledge(medicine, symptom) # 新增知識進資料庫
    elif int(intent)==1:
        medicine = input('請問要刪除的中藥材名稱是：')
        doctor.del_knowledge(medicine) # 移除資料庫的知識