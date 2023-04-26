# CoRider-Assignment

This project is a simple REST API built using Flask and MongoDB. It performs CRUD operations on a database of users.

## Setup (Development)

1. Clone the repository
   `git clone https://github.com/deadaf/CoRider-Assignment`
2. Rename `.example.env` to `.env` and fill in the required details.
3. Setup Environment.
   ```
   python3 -m venv env
   source env/bin/activate
   pip3 install -r requirements.txt
   ```
   OR (using `poetry`)<br>
   ```
   poetry install
   ```
4. Run the server using `python3 app.py`

## Setup using Docker

1. Build the Docker image:
   ```
   docker build -t myapp .
   ```
2. Run the Docker container:
   ```
   docker run -p 8001:8001 myapp
   ```

## Usage

### GET /users
Get a list of all users. <br>
![image](https://user-images.githubusercontent.com/72350242/234672368-d1cdcd0a-6a1d-4a86-b417-210ac5ca4964.png)

### GET /users/{id}
Get a user by their ID. <br>
![image](https://user-images.githubusercontent.com/72350242/234672784-393d4607-63cf-4062-958f-43a0ac01f465.png) <br>
![image](https://user-images.githubusercontent.com/72350242/234672820-4bee4cee-38f9-42dd-a40a-9e857ef288f5.png)

### POST /users
Create a new user. <br>
![image](https://user-images.githubusercontent.com/72350242/234673100-4705a873-b265-4002-b1f2-4ec6aacba61d.png)

### PUT /users/{id}
Update an existing user by their ID. <br>
![image](https://user-images.githubusercontent.com/72350242/234673396-9d8300e2-bb9a-4d95-a485-8e443c6ee3f0.png)

### DELETE /users/{id}
Delete a user by their ID. <br>
![image](https://user-images.githubusercontent.com/72350242/234673719-779ca0dc-c639-4511-8c9c-c63ba2d8b312.png)
![image](https://user-images.githubusercontent.com/72350242/234673673-e1a11947-594e-4df7-b56b-57671cfa5f9f.png)

