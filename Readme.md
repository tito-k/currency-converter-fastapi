docker build -t c-converter-image . // To build the docker imager
docker run -p 80:80 --name c-converter-container c-converter-image
//spin up a container with name c-converter-container from the docker image c-converter-image

http://localhost:8000/api/v1/currency-converter?from_currency=NGN&to_currency=EUR&amount=100