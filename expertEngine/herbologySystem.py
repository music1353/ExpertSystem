# coding: utf-8

import json
import codecs
import re

class expertSystem(object):
    def __init__(self, database_path):
        self.database_path = database_path
        
    def read_database(self):
        with codecs.open(self.database_path, 'r', 'utf-8') as f:
            database = json.load(f)
            return database
        
    def list_database(self):
        database = self.read_database()
        
        for db in database:
            print(db)
        
    def list_database_symptom(self):
        database = self.read_database()
        
        list_sym = []
        for db in database:
            for sym in db['symptom']:
                list_sym.append(sym)
                
        list_sym = {}.fromkeys(list_sym).keys()
        
        for li_sym in list_sym:
            print(li_sym, end=', ')
        
    def set_data(self, medicine, symptom):
        # symptom為list
        re_symptom = re.split(r"：|。|！|；|、|;|,|\?\s|;\s|,\s", symptom.replace(' ', '')) 
        item = {'medicine': medicine, 'symptom':re_symptom}
        return item
        
    def get_differ(self, predict, symptom):
        database = self.read_database()
        re_symptom = re.split(r"：|。|！|；|、|;|,|\?\s|;\s|,\s", symptom.replace(' ', ''))
        
        compairsion_symptom = []
        
        # search predict medicine's symptom
        for medicine in predict:
            for db in database:
                if medicine==db['medicine']:
                    compairsion_symptom.append(db['symptom'])
        
        # remove previous same symptom
        for item in compairsion_symptom:
            for sym in re_symptom:
                try:
                    item.remove(sym)
                except:
                    print('無需刪除項目')
                    pass
            
        return compairsion_symptom
    
    def re_callback(self, predict, symptom):
        compairsion_symptom = self.get_differ(predict, symptom)
        
        for i, medicine in enumerate(predict):
            for j, sym in enumerate(compairsion_symptom[i]):
                print('請問您有', sym, '的症狀嗎？ (Yes/No)')
                boolean_symptom = input('症狀：')
                if boolean_symptom=='Yes':
                    print('您可能需要', medicine, '中藥材')
                    break
                elif i==len(predict)-1 and j==len(compairsion_symptom[i])-1 and boolean_symptom=='No':
                    print('推薦給您', predict, '中藥材')
                elif boolean_symptom=='No':
                    continue
            else: continue
            break
            
    def run(self):
        identify = input('請問您的身份是(person/doctor)：')
    
        if(identify == 'person'):
            p = person(self.database_path)
        
            p.list_database_symptom()
            symptom = input('請問您的症狀是：')
        
            predict = p.match(symptom)
        
            if( predict==[] ):
                print('沒有這種中藥材呦')
            elif( len(predict)==1 ):
                print('您可能需要', predict, '中藥材')
            else:
                p.re_callback(predict, symptom)
              
        elif(identify == 'doctor'):
            d = doctor(self.database_path)
        
            intent = input('請問要新增中藥材(0), 還是刪除中藥材(1)：')
        
            if int(intent)==0:
                medicine = input('請問要新增的中藥材是：')
                symptom = input('適用症狀為：')
                d.add_knowledge(medicine, symptom)
            elif int(intent)==1:
                medicine = input('請問要刪除的中藥材名稱是：')
                d.del_knowledge(medicine)
                
                
class doctor(expertSystem):
    def add_knowledge(self, medicine, symptom):
        database = super().read_database()
        item = super().set_data(medicine, symptom)
        database.append(item)
        
        try:
            with codecs.open(self.database_path, 'w') as f:
                json.dump(database, f, ensure_ascii=False)
                
            print('成功新增', medicine, '中藥材！')
        except e:
            print('寫入失敗', e)
            
    def del_knowledge(self, medicine):
        database = super().read_database()
        
        re_medicine = list( re.split(r"：|。|！|；|、|;|,|\?\s|;\s|,\s", medicine.replace(' ', '')) )
        
        count = 0
        for med in re_medicine:
            for i, db in enumerate(database):
                if med==db['medicine']:
                    try:
                        database.pop(i)
                        count = count+1
                        print('成功刪除', med)
                    except e:
                        print('刪除', med, '錯誤', e)
        try:
            with codecs.open(self.database_path, 'w') as f:
                json.dump(database, f, ensure_ascii=False)
        except e:
            print('寫入失敗', e)

        if count>0:
            print('共刪除', count, '項中藥材')
        elif count==0:
            print('資料庫內沒有你要刪除的中藥材！')

            
class person(expertSystem):
    def match(self, symptom):
        predict = []
        database = super().read_database()
        re_symptom = list( re.split(r"：|。|！|；|、|;|,|\?\s|;\s|,\s", symptom.replace(' ', '')) )
        
        for re_sym in re_symptom:
            for db in database:
                if set(re_symptom).issubset(set(db['symptom'])) and len(re_symptom)>1:
                    predict.append(db['medicine'])
                    break;
                elif re_sym in db['symptom']:
                    predict.append(db['medicine'])
        
        predict = list(set(predict))
        
        return predict