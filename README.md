# build image
docker-compose build flask
# access container
docker-compose run --rm flask bash
# run flask dev
make dev
# generate scwr-api-requirements.json
make swagger
# access swagger through browser
http://container_ip:8888/swagger.json
# copy and paste json in editor.swagger.io to see rendered version
