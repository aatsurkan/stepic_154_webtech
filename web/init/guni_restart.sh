kill -TERM $(cat ~/web/pids/g_hello.pid)
kill -TERM $(cat ~/web/pids/g_ask.pid)
gunicorn -b 0.0.0.0:8080 -p ~/web/pids/g_hello.pid hello &
cd ask
gunicorn -b 0.0.0.0:8000 -p ~/web/pids/g_ask.pid ask.wsgi &
mysql -uroot -e "use ask; delete from auth_user where username = 'user1';"
