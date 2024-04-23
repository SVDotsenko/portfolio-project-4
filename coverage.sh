#!/bin/bash

if command -v python &> /dev/null || command -v python3 &> /dev/null
then
  echo -e "\033[41;37mRunning unit tests for Django\033[0m"
  rm -rf htmlcov
  coverage run --source='.' manage.py test
  coverage report -m
  coverage html
  rm .coverage
  start htmlcov/index.html
else
  echo -e "\033[41;37mPython is not installed\033[0m"
  start https://www.python.org/downloads/
fi

if command -v node &> /dev/null
then
  echo -e "\033[41;37mRunning unit tests for JavaScript\033[0m"
  rm -rf coverage
  npm run test
  start coverage/lcov-report/index.html
else
  echo -e "\033[41;37mNode.js is not installed\033[0m"
  start https://nodejs.org/en/download/
fi