@echo off

set GAME_SERVER=127.0.0.127
:start
"C:/Panda3D-1.8.1/python/ppython" -m pirates.piratesbase.PiratesStart
pause
goto :start
