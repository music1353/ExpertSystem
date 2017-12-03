# ExpertSystem

### 專案介紹
- - -
<p>以中藥材為主題，透過提供<strong>症狀(symptom)</strong>，專家系統會推薦適合的中<strong>藥材(medicine)</strong></p>
<p>person模式主要功能：提供症狀，系統會推薦藥材</p>
<p>doctor模式主要功能：新增、刪除database的knowledge</p>
<br />
  
### 檔案簡介
- - -
- expertEngine：專家系統推論模組
- knowledgeBase.json：知識庫（資料庫）
- database_data.py：列出database的資料的代碼
- database_symptom.py：列出database的symptom的代碼
- run_expertSystem.py：運行專家推論系統的代碼
<br />

### 下載方法
- - -
<p>專案右上點擊綠色按鈕(Clone or download)，選擇Download ZIP<p>
<br/>

### expertEngine Rest API
- - -
匯入模組：
<pre><code>import sys
sys.path.append('expertEngine') # 告訴系統模組位置
from expertEngine import herbologySystem as hs
</code></pre>
<br/>

指定database的路徑：
<pre><code>path = 'knowledgeBase.json' # database路徑
</code></pre>
<br/>

啟動expertEngine：
<pre><code>expertSystem = hs.expertSystem(path)
</code></pre>
<br/>

啟動<strong>person模式</strong>或是<strong>doctor模式</strong>的expertEngine(詳細類操作請參考<strong>各類方法</strong>)：
<pre><code>person = hs.person(path) # 啟動person模式
doctor = hs.doctor(path) # 啟動doctor模式
</code></pre>
<br/>

### 各類方法
- - -
Class expertSystem {
* __init__: (string)database_path</p>
* read_database(): <strong>return</strong> (list)database</p>
* list_database(): print all data database
* list_database_symptom(): print all symptom in database
* set_data( (string)medicine, (string, list)symptom ): in order to format data which need to store
* get_differ( (list)predict, (string, list)symptom ): delete same symptom in two or more predict medicine, will         <strong>return</strong> (list)compairsion_symptom
* re_callback( (list)predict, (string)symptom ): Q&A with left symptom to choose accurate medicine
* run(): run expertSystem(according to your identify then can do something)
<p>}</p>
</br>

Class doctor(expertSystem) {
* add_knowledge( (string)medicine, (string, list)symptom ): add new knowledge in database
* del_knowledge( (string)medicine ): delete medicine from database
<p>}</p>
</br>

Class person(expertSystem) {
* match( (string, list)symptom ): key in your symptom, then expertSystem will provide some medicine for you, <strong>return</strong> (list)predict
<p>}</p>
</br>

### 程式範例
- - -
啟動專家推論問答：
<pre><code>import sys
sys.path.append('expertEngine') # 告訴系統模組位置
from expertEngine import herbologySystem as hs

path = 'knowledgeBase.json'
eS = hs.expertSystem(path)

eS.run()
</code></pre>
<br/>

查看database資料：
<pre><code>import sys
sys.path.append('expertEngine')
from expertEngine import herbologySystem as hs

path = 'knowledgeBase.json' # database路徑
expertSystem = hs.expertSystem(path) # 啟動expertEngin

expertSystem.list_database() # 列出知識庫資料
</code></pre>
<br/>


查看目前database所有症狀：
<pre><code>import sys
sys.path.append('expertEngine')
from expertEngine import herbologySystem as hs

path = 'knowledgeBase.json' # database路徑
expertSystem = hs.expertSystem(path) # 啟動expertEngin

expertSystem.list_database_symptom() # 列出資料庫所有症狀
</code></pre>
<br/>


