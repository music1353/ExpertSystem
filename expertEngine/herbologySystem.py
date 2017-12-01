# coding: utf-8

import json
import codecs
import re

class expertSystem:
    def __init__(self, dataBase_path):
        self.dataBase_path = dataBase_path
        
    def read_dataBase(self):
        with codecs.open(self.dataBase_path, 'r', 'utf-8') as f:
            database = json.load(f)
            return database
        
    def list_database(self):
        database = self.read_dataBase()
        
        for db in database:
            print(db)
        
    def list_database_symptom(self):
        database = self.read_dataBase()
        
        list_sym = []
        for db in database:
            for sym in db['symptom']:
                list_sym.append(sym)
                
        list_sym = {}.fromkeys(list_sym).keys()
        
        for li_sym in list_sym:
            print(li_sym, end=', ')
        
    def set_data(self, medicine, symptom):
        # symptom為list
        re_symptom = re.split(r";|,|\?\s|;\s|,\s", symptom.replace(' ', '')) 
        item = {'medicine': medicine, 'symptom':re_symptom}
        return item
        
    def get_differ(self, predict, symptom):
        database = self.read_dataBase()
        
        compairsion_symptom = []
        
        # search predict medicine's symptom
        for medicine in predict:
            for db in database:
                if medicine==db['medicine']:
                    compairsion_symptom.append(db['symptom'])
        
        # remove previous same symptom
        for item in compairsion_symptom:
            item.remove(symptom)
            
        return compairsion_symptom
    
    def re_callback(self, predict, symptom):
        compairsion_symptom = self.get_differ(predict, symptom)
        
        for i, medicine in enumerate(predict):
            for sym in compairsion_symptom[i]:
                print('請問您有', sym, '的症狀嗎？ (Yes/No)')
                boolean_symptom = input('症狀：')
                if boolean_symptom=='Yes':
                    print('您可能需要', medicine, '中藥材')
                    break
                elif boolean_symptom=='No':
                    continue
            else: continue
            break
                
class doctor(expertSystem):
    def add_knowledge(self, medicine, symptom):
        database = super().read_dataBase()
        item = super().set_data(medicine, symptom)
        database.append(item)
        
        try:
            with codecs.open(self.dataBase_path, 'w') as f:
                json.dump(database, f, ensure_ascii=False)
                
            print('成功新增', medicine, '中藥材！')
        except e:
            print('寫入失敗', e)
            
    def del_knowledge(self, medicine):
        database = super().read_dataBase()
        
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
            with codecs.open(self.dataBase_path, 'w') as f:
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
        database = super().read_dataBase()
        re_symptom = list( re.split(r"：|。|！|；|、|;|,|\?\s|;\s|,\s", symptom.replace(' ', '')) )
        
        for db in database:
            if set(re_symptom).issubset(set(db['symptom'])):
                predict.append(db['medicine'])
        return predict