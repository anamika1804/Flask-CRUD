## Flask CRUD Application with MongoDB and Docker
This repository contains a Flask CRUD (Create, Read, Update, Delete) application integrated with MongoDB and Dockerized for easy deployment.

## Table of Contents
Prerequisites
Getting Started
1. Clone the Repository
2. Environment Variables
3. Build and Run the Docker Containers
4. Access the Application
Interacting with the API
Stopping the Application
Cleaning Up
Contributing
License
# Prerequisites
Before you begin, ensure you have the following installed on your system:

Docker
Docker Compose
## Getting Started
Follow these instructions to get the application up and running on your local machine.

# 1. Clone the Repository
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/anamika1804/flask-crud-docker.git
cd flask-crud-docker
# 2. Environment Variables
Create a .env file in the root directory of the project and add the following environment variable:

plaintext
Copy code
MONGO_URI=mongodb://mongo:27017/Users
This URI should match your MongoDB connection string. Update it as per your MongoDB setup.

# 3. Build and Run the Docker Containers
Build and start the Docker containers using Docker Compose:

bash
Copy code
docker-compose up --build
This command will build the Docker image for the Flask application and start both the Flask app and MongoDB containers.

# 4. Access the Application
Once the containers are up and running, you can access the Flask application at http://localhost:5000.

Interacting with the API
You can interact with the API using tools like curl or Postman. Here are some example API requests:

Get all users:

bash
Copy code
curl http://localhost:5000/users
Get a specific user by ID:

bash
Copy code
curl http://localhost:5000/users/<id>
Add a new user:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"name":"Jemmy", "email":"jem202@gmail.com", "password":"jemmy2002"}' http://localhost:5000/users
Update a user:

bash
Copy code
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Jemmy Updated", "email":"jem202@gmail.com", "password":"newpassword"}' http://localhost:5000/users/<id>
Delete a user:

bash
Copy code
curl -X DELETE http://localhost:5000/users/<id>
Stopping the Application
To stop the application and shut down the Docker containers, use Ctrl + C in the terminal where docker-compose up is running.

# Cleaning Up
To remove the Docker containers and network:

bash
Copy code
docker-compose down
This will stop and remove containers, networks, volumes, and images created by docker-compose up.
