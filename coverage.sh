#!/bin/bash
rm -rf coverage
npm run test
rm -rf htmlcov
coverage run --source='.' manage.py test
coverage report -m
coverage html
rm .coverage
cd htmlcov
rm .gitignore