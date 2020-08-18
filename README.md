# Remarkably code test

## Description
We need to record one-time "Events" and relate them to a User's data, such people moving out of an apartment building they own. These events are diverse in nature and could include things like a natural disaster, throwing a worldcup party for prospective tenents, hiring a new on-site property manager and so on. This can be plotted on a timeseries graph to provide visual cues about potential correlation between the event and the data.

### Functional Criteria

 1. The solution should not use existing databases or tables (done)
 2. The solution must expose an API surface that allows the following (done):
  ```
  a. `POST` new Event (done)
  b. `GET` a specfic Event (done)
  c. `GET` all Events (done)
  d. `GET` all Events related to a specific Item (done)
  ```
 3. The solution must protect requests by checking for and verifying a pre-shared secret header `x-rmb-eventscv-token` (done)
 
 ### Optional Criteria
 
 1. Include a "one-line" method for running the solution locally, such as a script file, docker compose, etc (done)
 2. Include an API endpoint that returns the following stats about Events:
   ```
   a. Total by type (done)
   b. Oldest event timestamp (done)
   c. Newest event timestamp (done)
   d. Item with most number of Events and its count
   ```
 3. Include API documentation that describes request and response parameters for each endpoint (done)

## Solution description

Solution is created using Flask microframework and postgres database. 

Automatic migrations of database (and seed data) are preformed after docker-compose up command.

Database connect:
```
'user': 'postgres',
'password': 'password',
'db': 'remarkably_db',
'host': 'localhost',
'port': '5431'
```
## Build and run

For starting postgres and API containers do the following in repo folder:

`docker-compose -f docker-compose.yml build` \
`docker-compose -f docker-compose.yml up -d`

This will start postgres container at port `5431` and API container at port `5000`

Database remarkably_db will be automatically created after docker-compose up.

## API documentation

Visit: `http://localhost:5000/api` for Swagger documentation (after docker-compose up).

## Postman collection for testing endpoints

Visit: `https://www.getpostman.com/collections/80234428fc21f36a0102`