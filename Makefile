init:
	pdm install

test:
	pdm run pytest -vvrP ./tests/

build:
	docker compose build

up:
	docker compose up -d

local:
	pdm run python -m vilbot

stop:
	docker compose stop

down:
	docker compose down

logs:
	docker compose logs
