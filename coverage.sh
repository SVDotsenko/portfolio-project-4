#!/bin/bash

echo -e "\033[41;37mRunning unit tests for Django\033[0m"
rm -rf htmlcov
coverage run --source='.' manage.py test
coverage report -m
coverage html
rm .coverage
start htmlcov/index.html

echo -e "\033[41;37mRunning unit tests for JavaScript\033[0m"
rm -rf coverage
npm run test
start coverage/lcov-report/index.html

cd htmlcov
rm .gitignore