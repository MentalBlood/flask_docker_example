# Simple dockerizable flask app using REST API

## Build
    docker build -t new_image .

## Run
    docker run -it --rm -d -p 8080:80 --name flask_docker_example new_image

## Use
Open [http://localhost:8080/a/b](http://localhost:8080/?a=1&b=3) in your browser. Instead of 1 and 3 you can provide any other integer numbers