FROM debian:10

# Install python
RUN apt-get update \
    && apt-get install -y python3 python3-pip

RUN pip3 install Flask

COPY . /app

# Expose the PostgreSQL port
EXPOSE 80

# Add VOLUMEs to allow backup of config, logs and databases

WORKDIR /app

# Set the default command to run when starting the container
CMD python3 app.py
