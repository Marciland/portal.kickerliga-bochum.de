# portal.kickerliga-bochum.de

This repository contains the code for the portal subdomain of the kickerliga-bochum.de website. The portal is designed to provide a space for team captains to manage their player lists.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [Deployment](#deployment)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used

- **Frontend**: Node.js v21.7.3
- **Backend**: Python 3.10

## Installation

### Frontend

To install the necessary dependencies, make sure you have Node.js (preferably v21.7.3) installed.
Then, run the following commands:

```sh
npm install
```

### Backend

To install the necessary dependencies, make sure you have Python3 (prefereably 3.10) installed.
Then, run the following commands:

```sh
pip install -r requirements.txt
```

## Running the Project

### Frontend

To run the frontend locally, use:

```sh
npm run dev
```

This will start the development server, and you can view the frontend in your browser at `http://localhost:5173`.

### Backend

To run the backend locally, use:

```sh
python main.py -d
```

This will start the development API, and you can view the API in your browser at `http://localhost:8001/docs`.

## Testing

### Frontend

To test the frontend locally, use:

```sh
npm run unit-test
npm run dev
npm run e2e-test
```

This will run unit tests and start the development server, to run end to end tests against it.

### Backend

To test the backend locally, use:

```sh
python -m pytest --cov=models --cov=modules
python -m coverage xml
```

This will run unit tests and show the coverage. The coverage xml command creates a merged xml for coverage visualization.

## Deployment

### Frontend

To build the frontend for production, run:

```sh
npm run build
```

This will generate the static HTML files that you need to serve.

### Backend

To build the API for production, run:

```sh
docker build --tag portal.kickerliga-bochum.de:latest .
docker run -d --restart always \
       --name portal.kickerliga-bochum.de \
       -p 0.0.0.0:8001:8001 \
       portal.kickerliga-bochum.de:latest
```

## Features

- Team captains can create player lists for their teams
- User-friendly interface built with Vue.js 3
- JWT secured API built with FastAPI 0.109.2

## Contributing

Contributions are not desired at this time. If you encounter any issues or have suggestions, please open an issue in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
