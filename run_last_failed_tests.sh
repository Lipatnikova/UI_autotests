#!/bin/bash

rm -Rf ./allure-results
pytest -v -s --last-failed --alluredir=./allure-results
allure serve ./allure-results
