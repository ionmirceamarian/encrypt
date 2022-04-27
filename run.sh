#!/bin/bash

docker-compose -f ./docker-compose.yml up -d --build --force-recreate

echo 'Waiting for API server to be up...'
response=0
while [ $response != 200 ]
do
  response=$(curl --write-out %{http_code} --silent --output /dev/null http://localhost:5000/status)
  echo ${response}
  if [ $response != 200 ]
  then
    sleep 3
  fi
done

echo Running migration for $(pwd)

docker exec -it backend flask db init
docker exec -it backend flask db migrate -m "Initial migration."
docker exec -it backend flask db upgrade

