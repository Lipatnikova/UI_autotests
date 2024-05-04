#!/bin/bash

workers=2
hub_address=http://192.168.1.236:4444/wd/hub

java -jar selenium-server-4.20.0.jar hub &
sleep 15

java -jar selenium-server-4.20.0.jar node --selenium-manager true &
sleep 15

rm -Rf ./allure-results
pytest -v -s -n=$workers --hub_address $hub_address --alluredir=./allure-results
allure serve ./allure-results
