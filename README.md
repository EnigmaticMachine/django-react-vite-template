# Django React Vite Starter Project

This repository serves as a starter template for developing web applications using Django for the backend and React with Vite for the frontend. It includes a Docker setup for easy environment management and deployment.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose
- Node.js and npm

### Clone the Repository

1. **Clone the repository:**
   ```sh
   git clone git@github.com:EnigmaticMachine/django-react-vite-template.git
   cd django-react-vite-template
   ```

### Running the Application

2. **Build and run Docker containers:**
   ```sh
   make dev-up
   ```

3. **Apply Django migrations:**
   ```sh
   make dev-migrate
   ```

4. **Create a superuser:**
   ```sh
   make dev-createsuperuser
   ```

### Accessing the Application

- The Django backend will be running at `http://localhost:8000`.
- The React frontend will be running at `http://localhost:5173`.
- The Nginx server will be running at `http://localhost:80` and will proxy requests to the backend and frontend services.

### Monitoring with Uptime Kuma

To set up and run the Uptime Kuma monitoring service:

1. **Build and run Docker containers for monitoring:**
   ```sh
   make monitoring-up
   ```

2. **Access Uptime Kuma dashboard:**
   - The Uptime Kuma monitoring dashboard will be running at `http://localhost:3001`.

## Configuration

### Environment Variables

The backend service configuration is managed via environment variables specified in the `.env`, `.env.dev`, and `.env.test` files. The `docker-compose` files will load these variables accordingly:

- `POSTGRES_DB`: Name of the PostgreSQL database.
- `POSTGRES_USER`: PostgreSQL username.
- `POSTGRES_PASSWORD`: PostgreSQL password.
- `DEBUG`: Django debug mode (set to `'1'` for development).
- `DJANGO_ALLOWED_HOSTS`: Allowed hosts for the Django application.
- `DJANGO_SECRET_KEY`: Secret key for Django.

### Docker Compose Services

- **db**: Runs the PostgreSQL database.
- **backend**: Runs the Django application.
- **frontend**: Runs the React frontend.
- **nginx**: Runs the Nginx server.
- **uptime-kuma**: Runs the Uptime Kuma monitoring service.

### Volume Management

- `postgres_data`: Stores the PostgreSQL data files.
- `uptime-kuma-data`: Stores Uptime Kuma data.

## Features

### Security

- **Environment Variables**: Managed using `django-environ`.
  - Sensitive information is stored in environment variables, not in the codebase.
  - `.env`, `.env.dev`, and `.env.test` files for different environments.
- **Django Security Middleware**: Enabled to ensure secure HTTP headers.


### Database

- **PostgreSQL**: Configured for production readiness.

### Performance

- **Compression**: Enabled Gzip and Brotli compression for responses.

### Maintainability

- **Code Quality**: Enforced with `black`, `pylint`, and `flake8`.
- **Documentation**: Auto-generated using `drf-spectacular` with Swagger integration.
- **Testing**:
  - Unit, integration, and end-to-end tests.
  - Database cleanup after each test.
- **Project Structure**:
  - Organized settings with separate files for base, test, dev, and prod configurations.
- **Makefile**:
  - Commands for tests, starting the local server, and starting the production server.

### Monitoring and Logging

- **Application Monitoring and Logging**:
  - Health endpoint added.
  - Separate logging settings for production and development.
  - Uptime Kuma setup for monitoring.
  - Custom `LogHttpRequestMiddleware` to track error response codes.

### Deployment

- **CI/CD Pipelines**:
  - Set up with GitHub Actions for continuous integration and deployment.
  - Workflows for running tests and linters.

## Running Tests

### Backend Tests

To run the backend tests:

1. **Build and run Docker containers for testing:**
   ```sh
   make test-run
   ```

### Frontend Tests

To be defined.

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is inspired by the need to have a unified starting point for building full-stack applications with Django and React.
