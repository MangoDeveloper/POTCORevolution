
set +v
export pUsername=Skipps
export pPassword=password
export LOGIN_TOKEN=$pUsername
export GAME_SERVER=127.0.0.1

echo ===============================
echo Starting Pirates Online...
echo Username: $pUsername$
echo Client Agent IP: $GAME_SERVER$
echo ===============================
python -m pirates.piratesbase.PiratesStart.py
pause
sleep 1
