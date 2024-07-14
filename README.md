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

### Volume Management

- `postgres_data`: Stores the PostgreSQL data files.

## Running Tests

### Backend Tests

To run the backend tests:

1. **Build and run Docker containers for testing:**
   ```sh
   make test-build
   make test-up
   ```

2. **Run tests:**
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
