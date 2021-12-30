source .venv/bin/activate > /dev/null 2>&1
doccano init
doccano createuser --username admin --password pass
doccano webserver --port 8000 &
doccano task &
sleep 10
echo Open localhost:8000 - username:admin - password:pass