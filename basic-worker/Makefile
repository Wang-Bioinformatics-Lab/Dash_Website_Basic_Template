build:
	docker build -t gnpslibrary . 

bash:
	docker run -it --rm gnpslibrary /bin/bash

server-compose-build-nocache:
	docker-compose --compatibility build --no-cache

server-compose-interactive:
	docker-compose --compatibility build
	docker-compose --compatibility up

server-compose:
	docker-compose --compatibility build
	docker-compose --compatibility up -d

attach:
	docker exec -i -t gnpslcms-dash /bin/bash
