# DRF-dataTable-Example-server-side
DataTables Example (server-side) - Python Django REST framework

* [Youtube Demo]() - 建議看影片的 demo 說明

DataTables (server-side) 搭配 [Django REST framework](http://www.django-rest-framework.org/) 簡單範例 📝

## 特色
* 使用 [Django REST framework](http://www.django-rest-framework.org/) 建立API。
* 搭配 [ DataTables ]( https://datatables.net/ ) 並且使用 [ server-side ]( https://datatables.net/manual/server-side ) 增加使用者體驗。
* 搭配 Bootstrap 。
* 搭配 SQLite ( 10萬比模擬資料 )。


## 安裝套件

請在你的命令提示字元 (cmd ) 底下輸入

安裝 [Django](https://github.com/django/django)

>pip install django

安裝 [Django-REST-framework](http://www.django-rest-framework.org/)
>pip install djangorestframework



## 說明

* LOG 資訊非常重要，可以參考官網 [django logging](https://docs.djangoproject.com/en/1.11/topics/logging/) , 或是看範例裡面的 [settings.py ]()裡面的 LOGGING。

* 建議透過 [django-db-backends](https://docs.djangoproject.com/en/1.11/topics/logging/#django-db-backends) 來觀看目前的 orm 到底執行了什麼 SQL 指令。


## 執行方法

使用命令提示字元 ( cmd ) 輸入下方指令

>  python manage.py runserver

然後瀏覽

[http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/)

## 執行畫面

#### 首頁
##### [Get] api/music/{額外 DataTables 參數}
![alt tag](http://i.imgur.com/PaYzAU4.jpg)

#### 新增
##### [POST] api/music/
![alt tag](http://i.imgur.com/fwOxMwr.jpg)

#### 編輯
##### [PUT] api/music/{id}/
![alt tag](http://i.imgur.com/3MOF4ud.jpg)

#### 刪除
##### [DELETE] api/music/{id}/
![alt tag](http://i.imgur.com/s48Tl6S.jpg)

#### 搜尋  排序
##### [Get] api/music/{額外 DataTables 參數}
![alt tag](http://i.imgur.com/Ndvm3bu.jpg)




## 後記

* 從影片中的 demo 可以很明顯的看出當資料量很大（5 萬比）的時候，如果沒有用 server-side 的方式，而是一次全部載入，使用者體驗非常差。

* 本範例前後端並沒有分離，而是寫在一起，比較好的方式，應該是前後端分離。



## 執行環境
* Python 3.4.3

## Reference
* [Django REST framework](http://www.django-rest-framework.org/)
* [ DataTables ]( https://datatables.net/ )
* [ Bootstrap ]( http://getbootstrap.com/ )

## License
MIT license