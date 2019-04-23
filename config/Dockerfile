FROM python:3.6-slim

WORKDIR /var/app

COPY . /var/app

USER root

RUN useradd -ms /bin/bash webapp

RUN chown -R webapp /var/app

RUN chmod 755 /var/app

RUN apt-get update \
    && apt-get install -y make \
    && pip install pipenv

USER webapp

RUN pipenv install --dev

# needed for the package to be recognized by python
ENV PYTHONPATH /var/app

EXPOSE 8888

CMD ["bash"]
