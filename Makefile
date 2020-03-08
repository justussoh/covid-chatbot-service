deploy:
	gcloud app deploy app.yaml --project covid-19-chatbot-270500

install:
	pip install -r requirements.txt

run-local:
	pipenv run gunicorn -w 1 main:app

run-local-pepe:
	gunicorn --reload -w 1 main:app