1. в settings.py отрегулировать всё под себя <br>
2. запустить редис (sudo service redis-server start) <br>
3. daphne sites.asgi:application или python manage.py runserver (у кого-то работает, у кого-то нет) <br>
4. запустить селери (celery -A sites worker -l info либо celery -A sites worker -l info --pool=solo) <br>
