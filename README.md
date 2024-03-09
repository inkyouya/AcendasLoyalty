# Requirements
You will need docker and docker-compose to run this project. You can find the installation instructions for them here:

- Docker installation: https://docs.docker.com/engine/install/
- Docker compose installation: https://docs.docker.com/compose/install/

# Setup instructions
After cloning the project into a local directory and setting up docker, you will need to do the following:

## Building the image
Build the application with `docker-compose build`

## Setting up environment variables
With `.sample-env` as a guide, create a file to store all the environment variables that the application needs. For local development, you can use the default values without setting a value for them. That means you just have to use the `Basic configuration for local development` section in `.sample-env`

## Running the project
Start the application with `docker-compose up`

# Usage
After setting up the application, you should be able to acess the hotel search endpoint via `http://localhost/hotel/` with the following GET parameters as search fields:
- `destination`: Search based on a single given desitnation ID
- `hotels`: Search based on a list of hotel IDs

An example URL with a destination + multiple hotel search will look like:
>http://localhost:80/hotel/?hotels=SjyX&destination=5432&hotels=iJhz

