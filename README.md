# README

我寫了 `docker-compose.yaml` 、 `Back-End/Dockerfile` 作為模板

因為一組可能 **不會只需要一個 Docker**

例如資料庫就用了兩個：`mongo`、`mongo-express` (參考 `docker-compose.yaml`)

後端則是以 Python 的 Docker 為基礎，

透過 `Back-End/requirements.txt` 安裝了其他必要相依套件 (參考 `Back-End/Dockerfile`)

所以不是一個 Dockerfile 就可以搞定的！

## 要做的事

- **Fork 這個 Repo**
- 請組長改一下 `docker-compose.yaml`，寫入你需要的東西
- 在各組目錄加入 Dockerfile 和任何你覺得必要的檔案，讓他變成你心目中的模樣
- 改好以後 **發個 PR 給我** 吧，讓你我都練習一下 Git 的使用 XD

## 這只是模板

四個目錄的分配只是我心目中，目前想像的、覺得我們專案應該有的長相

正式動工時也許不會完全一樣

再說一次，這不是我們正式的 Repo ！！！

## 練習

`docker-compose up -d`

接著看看 127.0.0.1:8080

應該可以看到 Hi? 的字樣

127.0.0.1:8081 則可以看到 Mongo Express 的介面

## 共筆

https://hackmd.io/@AlaRduTP/docker-notes/edit

這是我隨手記下的一點點重點，也許會對你有些幫助

因為沒有好好的整理

歡迎共編讓他更豐富精彩～
