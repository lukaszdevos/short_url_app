path =.
clean_code:
	docker-compose run --rm backend isort $(path)
	docker-compose run --rm backend black $(path)

start-local:
	docker-compose up -d

stop-local:
	docker-compose stop

restart-local:
	docker-compose restart

build:
	docker-compose up -d --build

test:
	docker-compose run --rm backend coverage run -m pytest -vv
	docker-compose run --rm backend coverage report

shell:
	docker-compose run --rm backend python manage.py shell