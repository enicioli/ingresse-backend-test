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
sudo docker-compose build && sudo docker-compose up -d
```
Two containers will be initialized:
- ingresse-backend-test-mongo (MongoDB)
- ingresse-backend-test-app (REST API connected to the host port 5000)

#### Database
![Relationship Entity Diagram](https://github.com/enicioli/ingresse-backend-test/blob/master/resources/DER.jpg)

### Tests
@todo

## REST API
@todo

#### Main technologies
- [Docker](https://www.docker.com/)
- [Python3](https://www.python.org/)
- [MongoDB](https://www.mongodb.com/)
- [Flask](https://palletsprojects.com/p/flask/)
- [MongoFrames MongoDB ODM](http://mongoframes.com/)
- [JSON Schema](http://json-schema.org/)