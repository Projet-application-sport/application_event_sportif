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
	docker login 
	docker tag $(USERNAME)/$(IMAGE):$(TAG) $(USERNAME)/$(IMAGE):latest
	docker push $(USERNAME)/$(IMAGE):latest
