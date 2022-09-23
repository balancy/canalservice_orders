#!/bin/bash

set -e

echo "Приведение репозитория к актуальному состоянию"
git pull

echo "Запуск docker контейнеров"
sudo docker-compose build
sudo docker-compose up -d

echo "Удаление устаревших и неиспользуемых docker сущностей"
sudo docker system prune -f

echo "Проект задеплоен"