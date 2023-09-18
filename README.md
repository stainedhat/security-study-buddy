# security-study-buddy
An API to help studying for security engineering interviews

### Overview
This project is a simple API to help study for security engineering interviews. It is a work in progress and very much rough around the edges. The goal is to keep skills fresh, build something interesting, and provide some useful value.

### Architecture
#### API: FastAPI
The backend for this is a FastAPI server that provides a set of CRUD actions to manage questions and answers

#### Frontend: ?
Frontend is TBD

#### Data: sqlite (for now)
Backend is currently sqlite while in development but the API uses sqlalchemy so swapping to something like Postgres will be easy.

### Deployment
Eventually this will be deployed via kubernetes but for now it's just local docker for dev.