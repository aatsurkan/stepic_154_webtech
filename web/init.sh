sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
cd ~/web/hello
gunicorn -b 0.0.0.0:8080 -p ~/web/pids/g_hello.pid hello:app &
cd ~/web/ask
gunicorn -b 0.0.0.0:8000 -p ~/web/pids/g_ask.pid ask.wsgi &
sudo /etc/init.d/mysql restart
sudo chmod +x manage.py
./manage.py syncdb
