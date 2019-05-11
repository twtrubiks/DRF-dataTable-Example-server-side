# DRF-dataTable-Example-server-side

此版本為 Django>2.0，以及搭配 MySQL 5.7 的範例

```text
Django==2.2.1
djangorestframework==3.9.3
```

如果使用 Django<2.0，請參考 [master branch](https://github.com/twtrubiks/DRF-dataTable-Example-server-side)

DataTables Example (server-side) - Python Django REST framework

* [Youtube Demo](https://youtu.be/E0Pf5Ci-vGw) - 建議看影片的 demo 說明

DataTables (server-side) 搭配 [Django REST framework](http://www.django-rest-framework.org/) 簡單範例 📝

## 特色

* 使用 [Django REST framework](http://www.django-rest-framework.org/) 建立API。
* 搭配 [DataTables]( https://datatables.net/ ) 並且使用 [server-side]( https://datatables.net/manual/server-side ) 增加使用者體驗。
* 搭配 Bootstrap 。
* 搭配 MySQL 5.7。

## 安裝套件

請在你的命令提示字元 (cmd ) 底下輸入

安裝 [Django](https://github.com/django/django)

這邊請注意，**Django==2.2.1**

>pip install Django==1.11.20

安裝 [Django-REST-framework](http://www.django-rest-framework.org/)
>pip install djangorestframework

安裝 [django-model-utils](https://django-model-utils.readthedocs.io/en/latest/index.html)
>pip install django-model-utils

或是使用 cmd (命令提示字元)

```cmd
pip install -r requirements.txt
```

## MySQL

使用 docker 建立 MySQL

```cmd
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password123 -d mysql:5.7
```

## 說明

* LOG 資訊非常重要，可以參考官網 [django logging](https://docs.djangoproject.com/en/1.11/topics/logging/) , 或是看範例裡面的  [settings.py](https://github.com/twtrubiks/DRF-dataTable-Example-server-side/blob/master/drf_table_ex/settings.py) 裡面的 LOGGING。

* 建議透過 [django-db-backends](https://docs.djangoproject.com/en/1.11/topics/logging/#django-db-backends) 來觀看目前的 orm 到底執行了什麼 SQL 指令，可以到範例裡面的 [settings.py](https://github.com/twtrubiks/DRF-dataTable-Example-server-side/blob/master/drf_table_ex/settings.py) 找 django.db.backends。

## 執行方法

使用命令提示字元 ( cmd ) 輸入下方指令

> python manage.py runserver

然後瀏覽

[http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/)

## 執行畫面

### 首頁

#### [Get] api/music/{額外 DataTables 參數}

![alt tag](http://i.imgur.com/PaYzAU4.jpg)

### 新增

#### [POST] api/music/

![alt tag](http://i.imgur.com/fwOxMwr.jpg)

### 編輯

#### [PUT] api/music/{id}/

![alt tag](http://i.imgur.com/3MOF4ud.jpg)

### 刪除

#### [DELETE] api/music/{id}/

![alt tag](http://i.imgur.com/s48Tl6S.jpg)

### 搜尋  排序

#### [Get] api/music/{ 額外 DataTables 參數 }

![alt tag](http://i.imgur.com/Ndvm3bu.jpg)

## 後記

* 從影片中的 demo 可以很明顯的看出當資料量很大（5 萬筆）的時候，如果沒有用 server-side 的方式，而是一次全部載入，使用者體驗非常差。

* 本範例前後端並沒有分離，而是寫在一起，比較好的方式，應該是前後端分離。

* api document 可參考 [api_document.html](https://github.com/twtrubiks/DRF-dataTable-Example-server-side/blob/master/api_document.html) ，直接用瀏覽器開啟即可。 ( 文件教學可參考  [aglio_tutorial](https://github.com/twtrubiks/aglio_tutorial) )

![](http://i.imgur.com/xOe8qsD.png)

## 更換 MySQL 資料庫

因為有些人反映換成 MySQL 之後無法 work，所以我測試了一下，

步驟一，先要多安裝兩個套件，

安裝 PyMySQL

```cmd
pip install PyMySQL
```

安裝 mysqlclient

```cmd
pip install mysqlclient
```

( 這個有可能安裝不起來，我自己最後是去找 mysqlclient-1.4.2-cp36-cp36m-win32.whl 安裝成功 )

[settings.py](https://github.com/twtrubiks/DRF-dataTable-Example-server-side/blob/master/drf_table_ex/settings.py#L84) 要改成

```python
......

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo',
        'USER': 'root',
        'PASSWORD': 'password123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

......
```

也可參考之前的文章 [Django 如何連結 MySQL](https://github.com/twtrubiks/django-transactions-tutorial#django-%E5%A6%82%E4%BD%95%E9%80%A3%E7%B5%90-mysql)，

這邊要特別注意，MySQL 我使用 5.7，如果使用 MySQL 8.0，會遇到 django.db.utils.OperationalError: (2059, )

的問題，原因是 MySQL 8.0 的密碼加密方式改成了 caching_sha2_password，要再自行修改，簡單一點就是使用

MySQL 5.7。

## 執行環境

* Python 3.6.6

## Reference

* [Django REST framework](http://www.django-rest-framework.org/)
* [DataTables]( https://datatables.net/ )
* [Bootstrap]( http://getbootstrap.com/ )
* [django-model-utils](https://django-model-utils.readthedocs.io/en/latest/index.html)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
