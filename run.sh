source venv/bin/activate
nohup gunicorn -b 0.0.0.0:8080 -w 4 main:app > logs.log &