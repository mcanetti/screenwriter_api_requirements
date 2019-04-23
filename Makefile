.PHONY: flask dev lint test swagger

PORT?=8888
RUN=pipenv run

flask:
	$(RUN) gunicorn serv.entrypoint:app -c config/gunicorn.conf.py

dev:
	$(RUN) flask run --host 0.0.0.0 --port $(PORT) --reload --no-debugger

lint:
	$(RUN) flake8 serv tests

test: lint
	$(RUN) pytest -vv \
	  --cov serv \
		--cov-report xml \
		--cov-report term \
		--cov-config .coveragerc \
		--junit-xml=results.xml \
		tests/

swagger:
	$(RUN) flask swagger > scwr-api-requirements.json
