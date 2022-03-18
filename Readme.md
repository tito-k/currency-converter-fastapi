<h1>
	Currency Converter REST API.
</h1>

![Github-A Build Status](https://github.com//Nyior/django-rest-paystack/actions/workflows/lint_and_test.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/django-rest-paystack.svg)](https://badge.fury.io/py/django-rest-paystack)


## What is this about?
It's a minimal REST API that helps you figure out how much  let's say a dollar is worth in naira at the moment or at some date in the past.

## Getting Started Locally
The easiest way to get this project up and running locally is with Docker. You can get it [here](https://www.docker.com/products/docker-desktop/). With Docker setup on your PC, take the following steps to run this application locally:
- Clone this repo to your local machine
- Create a `.env` file in the root directory
- Copy the content of `.env-example` and paste it in your newly created `.env` file.

**make sure to replace `API_KEY` with a valid key** I've submitted a valid api-key that you could use along with the link to this repo

- Run the command `docker build -t c-converter-image .` in the root directory to build your docker image
- Run the command `docker run -p 80:80 --name c-converter-container c-converter-image` to spin up your container

http://localhost:8000/api/v1/currency-converter?from_currency=NGN&to_currency=EUR&amount=100

