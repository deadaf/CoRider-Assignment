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
   ````
   docker build -t myapp .```
   ````
2. Run the Docker container:
   ```
   docker run -p 8001:8001 myapp
   ```
