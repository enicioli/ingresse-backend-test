# Ingresse Backend Test

## Dependencies
- [Docker](https://www.docker.com/)

## Installation
```shell script
git clone https://github.com/enicioli/ingresse-backend-test.git
```
```shell script
cd ingresse-backend-test
```
```shell script
sudo docker-compose up -d --build
```
Two containers will be initialized:
- ingresse-backend-test-mongo (MongoDB)
- ingresse-backend-test-app (REST API connected to the host port 5000)

#### Database
![Relationship Entity Diagram](https://github.com/enicioli/ingresse-backend-test/blob/master/resources/DER.jpg)

>When the containers are running in development mode, some sample data is imported to the database.
This sample data is based in this [files](https://github.com/enicioli/ingresse-backend-test/tree/master/resources) *_samples.json

### Tests
```
sudo docker exec -it ingresse-backend-test-app sh -c "python3 -m pytest"
```

## REST API
```
POST    /event                         (Creates a new event)
GET     /event/:event_id               (Retrieves a specific event)
PATCH   /event/:event_id               (Updates a specific event - partial)
PUT     /event/:event_id               (Updates a specific event - full)
DELETE  /event/:event_id               (Removes a specific event)
GET     /event?q=:query                (Searches events filtered by a json formatted mongodb query)

POST    /interest/event/:event_id      (Creates a new event interest)
GET     /interest/:interest_id         (Retrieves a specific event interest)
DELETE  /interest/:interest_id         (Removes a specific event interest)
GET     /interest/email/:email         (Retrieves event interests for a specific customer by their email)
```

#### Main technologies
- [Docker](https://www.docker.com/)
- [Python3](https://www.python.org/)
- [MongoDB](https://www.mongodb.com/)
- [Flask](https://palletsprojects.com/p/flask/)
- [MongoFrames MongoDB ODM](http://mongoframes.com/)
- [JSON Schema](http://json-schema.org/)
- [pytest](https://docs.pytest.org/)