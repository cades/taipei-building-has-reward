# 專案說明
check_and_push.sikuli 這隻 crawler script 以 ronny 爬下來的[台北建管處建照記錄](http://tpebuilding.g0v.ronny.tw)為資料來源，撈出有「獎勵」關鍵字的執照之url, 存在 record.txt 內。  
因為開發時用的瀏覽器是Safari, 故目前只能在Mac OS X 上執行. （若改成用Google Chrome / Firefox 就能跨平台了）  

# 環境設定
跑script時要打開「Safari」和「Terminal」兩個應用程式。script會在這兩個app間來回切換。  
請上github fork一份（記得選ssh, 不要選https, 否則push時會要求輸入username/password），並打開Terminal, cd到專案目錄下.  
Safari則打開ronny的建照記錄網頁，選一張建照。script會從該張建照開始，往它的上一張爬。  
  
這樣就好了.  script會自動把抓到的url append到record.txt的檔尾，並把這份更動commit、push回去。  

如果你有爬出一些東西，歡迎發pull request給我。

# 注意事項
1. 由於sikuli運用螢幕截圖，跑script時不能做自己的事，建議在睡覺或電腦不用的時候放著讓它爬。  
2. 一張不含「獎勵」關鍵字的建照爬完約40秒，以一年400張建照計，約4.5hr可以跑完一年份的建照。
3. script中有一個delay(4), 那是為了等瀏覽器下載、顯示圖片。如果你所處的環境網路不夠快，這個值可以設大一點。(如果圖片還沒讀完就開始跑...可能會中途crash :P)

