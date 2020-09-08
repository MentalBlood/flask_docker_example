# Simple dockerizable flask app using REST API

## Build
    docker build -t new_image .

## Run
    docker run -it --rm -d -p 8080:80 --name flask_docker_example new_image

## Use
Open [http://localhost:8080/a/b](http://localhost:8080/a/b) in your browser. Instead of a and b you can provide integer numbers