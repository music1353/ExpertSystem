# ExpertSystem

### 專案介紹
- - -
<p>以中藥材為主題，透過提供<strong>症狀(symptom)</strong>，專家系統會推薦適合的中<strong>藥材(medicine)</strong><p>
  
  
### 檔案簡介
- - -
- expertEngine：專家系統推論模組
- knowledgeBase.json：知識庫（資料庫）
- database_data.py：列出database的資料的代碼
- database_symptom.py：列出database的symptom的代碼
- run_expertSystem.py：運行專家推論系統的代碼


### 下載方法
- - -
<p>專案右上點擊綠色按鈕(Clone or download)，選擇Download ZIP<p>


### expertEngine API
- - -
匯入模組：
<pre><code>import sys
sys.path.append('expertEngine') # 告訴系統模組位置
from expertEngine import herbologySystem as hs
</code></pre>

指定database的路徑：
<pre><code>path = 'knowledgeBase.json' # database路徑
</code></pre>

啟動expertEngine：
<pre><code>expertSystem = hs.expertSystem(path)
</code></pre>
