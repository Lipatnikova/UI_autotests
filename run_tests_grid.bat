@echo off

set workers=2
set hub_address=http://192.168.1.236:4444/wd/hub
set browser_name=edge

start java -jar selenium-server-4.20.0.jar hub
timeout /t 15
start java -jar selenium-server-4.20.0.jar node --selenium-manager true
timeout /t 15
start pytest -v -s -n=%workers% --hub_address %hub_address% --browser_name %browser_name%