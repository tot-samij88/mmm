up:
	docker-compose --file docker-compose.yml up
build:
	docker-compose --file docker-compose.yml build
up-build:
	docker-compose --file docker-compose.yml up --build
start-background:
	docker-compose --file docker-compose.yml up --build -d
makemigrations:
	docker-compose exec ex-backend python manage.py makemigrations
migrate:	
	docker-compose exec ex-backend python manage.py migrate
createsuperuser:	
	docker-compose exec ex-backend python manage.py createsuperuser
pairs:
	docker-compose exec ex-backend python manage.py distribution_pairs