sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

sudo rm /etc/gunicorn.d/hello.py
sudo ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py

sudo /etc/init.d/nginx restart
gunicorn /home/box/web/hello:app
