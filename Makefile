USERNAME=deborahbdh
IMAGE=footevent
TAG:=$(shell TZ=UTC date +"%Y%m%d")


all:

build:
	docker build -t $(USERNAME)/$(IMAGE):$(TAG) .

run:
	docker-compose up

test: build
	docker run -it $(USERNAME)/$(IMAGE):$(TAG) pipenv run pytest

deliver:
	docker tag $(USERNAME)/$(IMAGE):$(TAG) $(USERNAME)/$(IMAGE):latest
	docker push $(USERNAME)/$(IMAGE):latest
