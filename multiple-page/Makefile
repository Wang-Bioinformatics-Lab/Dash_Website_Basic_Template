server-compose-build-nocache:
	docker-compose --compatibility build --no-cache

server-compose-interactive:
	docker-compose --compatibility build
	docker-compose --compatibility up

server-compose:
	docker-compose --compatibility build
	docker-compose --compatibility up -d

dev-dash1:
	python ./dash_interface1.py

attach:
	docker exec -i -t template-dash /bin/bash
