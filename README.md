# Django shop order demo

## 相關指令
* 初始化product資料: `python manage.py loaddata */fixtures/initial_*`
* celery: `python shop_web/celery_app.py `
* 啟動redis:`redis-server`
* 啟動單元測試：`python manage.py test`

### GCP
* git
* sudo apt install python3-pip
* pip install -r
* makemigrations
* migrate
* loaddata
* nginx
* redis
    * sudo apt-get install redis-server
* gunicorn
    * pip install 
    * `sudo gunicorn -w 4 -b 127.0.0.1:8080 shop_web.wsgi:application –reload –max-requests 1`
* supervisor
    * sudo apt install supervisor
```
[supervisord]
directory=/var/www/django-shop-order-demo/shop_web/
command=sudo gunicorn -w 4 -b 127.0.0.1:8080 shop_web.wsgi:application –reload –max-requests 1
autostart=true
autorestart=true
stderr_logfile=/var/log/django-shop-order-demo.err.log
stdout_logfile=/var/log/django-shop-order-demo.out.log
```   

### Ref
* [Testing in Django](https://docs.djangoproject.com/en/2.2/topics/testing/)
* [Attempt to write a readonly database - Django w/ SELinux error](https://stackoverflow.com/questions/21054245/attempt-to-write-a-readonly-database-django-w-selinux-error)
* [使用 supervisor 管理进程](http://liyangliang.me/posts/2015/06/using-supervisor/)
* [docker-django-celery-tutorial](https://github.com/twtrubiks/docker-django-celery-tutorial)
* [Django + Celery + Redis + Gmail 實現異步寄信](https://medium.com/@zoejoyuliao/django-celery-redis-gmail-%E5%AF%84%E4%BF%A1-375904d4224c)
