# Django React Vite Starter Project

This repository serves as a starter template for developing web applications using Django for the backend and React with Vite for the frontend. It includes a Docker setup for easy environment management and deployment.


## Setup Instructions

### Prerequisites

- Docker and Docker Compose
- Node.js and npm

### Backend Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/EnigmaticMachine/DjangoBasicTemplate.git
   cd your-repo
   ```

2. **Build and run Docker containers:**
   ```sh
   docker-compose up --build
   ```

3. **Apply Django migrations:**
   ```sh
   docker-compose exec web python manage.py migrate
   ```

4. **Create a superuser:**
   ```sh
   docker-compose exec web python manage.py createsuperuser
   ```

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```sh
   cd frontend
   ```

2. **Install dependencies:**
   ```sh
   npm install
   ```

3. **Run the development server:**
   ```sh
   npm run dev
   ```

### Accessing the Application

- The Django backend will be running at `http://localhost:8000`.
- The React frontend will be running at `http://localhost:3000`.

## Configuration

### Environment Variables

The backend service configuration is managed via environment variables specified in the `docker-compose.yml` file:

- `POSTGRES_DB`: Name of the PostgreSQL database.
- `POSTGRES_USER`: PostgreSQL username.
- `POSTGRES_PASSWORD`: PostgreSQL password.
- `DEBUG`: Django debug mode (set to `'1'` for development).
- `DJANGO_ALLOWED_HOSTS`: Allowed hosts for the Django application.

### Docker Compose Services

- **db**: Runs the PostgreSQL database.
- **web**: Runs the Django application.

### Volume Management

- `postgres_data`: Stores the PostgreSQL data files.

## Running Tests

### Backend Tests

TODO

### Frontend Tests

TODO


## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is inspired by the need to have a unified starting point for building full-stack applications with Django and React.
