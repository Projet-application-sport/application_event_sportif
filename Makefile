USERNAME:=sofiane938
IMAGE :=appli-flask
TAG:=20190829

all:

build:
	docker build -t $(USERNAME)/$(IMAGE):$(TAG) .

run:
	docker run -it -p5000:5000 $(IMAGE):$(TAG) 

test:
	docker run -it $(USERNAME)/$(IMAGE):$(TAG) pipenv run pytest

deliver:
	echo "$(DOCKER_PASSWORD)" | docker login -u "$(DOCKER_USERNAME)" --password-stdin 
	docker tag $(USERNAME)/$(IMAGE):$(TAG) $(USERNAME)/$(IMAGE):latest
	docker push $(USERNAME)/$(IMAGE):latest
