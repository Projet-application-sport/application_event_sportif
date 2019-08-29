FROM python:3.7-buster

# Install python
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev

RUN pip3 install pipenv mysqlclient

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

WORKDIR /app

RUN pipenv install

# Expose the PostgreSQL port
EXPOSE 80

COPY . /app

# Add VOLUMEs to allow backup of config, logs and databases

# Set the default command to run when starting the container
CMD pipenv run python3 app/application_web_event.py
