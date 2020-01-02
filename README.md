# Face Recognition - Docker image

This project provides a docker image which offers a web service to recognize known faces on images. It's based on the great [ageitgey/face_recognition](https://github.com/ageitgey/face_recognition) project and just add a web service using the Python `face_recognition`-library.

<a href="https://www.buymeacoffee.com/JanLoebel" rel="Buy me a coffee!">![Foo](https://cdn.buymeacoffee.com/buttons/default-orange.png)</a>

## Get started

### Build the Docker image

Start by building the docker image with a defined name. This can take a while.

```bash
docker build -t facerec_service .
```

### Run the Docker image

Start the image and forward port 8080. Optionally bind a local directory to `/root/faces` to provide a location for predefined images which will be registered at start time.

```bash
docker run -d -p8080:8080 -vfaces:/root/faces facerec_service
```

## Features

### Register known faces

Simple `POST` an image-file to the `/faces` endpoint and provide an identifier.
`curl -X POST -F "file=@person1.jpg" http://localhost:8080/faces?id=person1`

### Read registered faces

Simple `GET` the `/register` endpoint.
`curl http://localhost:8080/faces`

### Identify faces on image

Simple `POST` an image-file to the web service.
`curl -X POST -F "file=@person1.jpg" http://localhost:8080/`

## Examples

In the `examples`-directory there is currently only one example that shows how to use the Raspberry Pi-Camera module to capture an image and `POST` it to the `Face Recognition - Docker image` to check for known faces.

## Notes

I'm not a Python expert, so I'm pretty sure you can optimize the Python code further :) Please feel free to send PR's or open issues.