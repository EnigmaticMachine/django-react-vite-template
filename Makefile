# Variables
DC = docker compose
DEV_COMPOSE_FILE = docker-compose.dev.yml
TEST_COMPOSE_FILE = docker-compose.test.yml
PROD_COMPOSE_FILE = docker-compose.prod.yml
MONITORING_COMPOSE_FILE = docker-compose.monitoring.yml


# Default target
.PHONY: help
help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Development targets
.PHONY: dev-build
dev-build: ## Build the Docker images for development
	$(DC) -f $(DEV_COMPOSE_FILE) build

.PHONY: dev-up
dev-up: ## Start the Docker containers for development
	$(DC) -f $(DEV_COMPOSE_FILE) up -d

.PHONY: dev-down
dev-down: ## Stop the Docker containers for development
	$(DC) -f $(DEV_COMPOSE_FILE) down

.PHONY: dev-logs
dev-logs: ## Follow logs of Docker containers for development
	$(DC) -f $(DEV_COMPOSE_FILE) logs -f

.PHONY: dev-migrate
dev-migrate: ## Run database migrations for development
	$(DC) -f $(DEV_COMPOSE_FILE) run backend python manage.py makemigrations
	$(DC) -f $(DEV_COMPOSE_FILE) run backend python manage.py migrate

.PHONY: dev-createsuperuser
dev-createsuperuser: ## Create a superuser for development
	$(DC) -f $(DEV_COMPOSE_FILE) run backend python manage.py createsuperuser

.PHONY: dev-shell
dev-shell: ## Open a Django shell for development
	$(DC) -f $(DEV_COMPOSE_FILE) run backend python manage.py shell

.PHONY: dev-clean
dev-clean: ## Clean up Docker containers, images, and volumes for development
	$(DC) -f $(DEV_COMPOSE_FILE) down -v --rmi all --remove-orphans

# Testing targets
.PHONY: test-build
test-build: ## Build the Docker images for testing
	$(DC) -f $(TEST_COMPOSE_FILE) build

.PHONY: test-up
test-up: ## Start the Docker containers for testing
	$(DC) -f $(TEST_COMPOSE_FILE) up -d

.PHONY: test-down
test-down: ## Stop the Docker containers for testing
	$(DC) -f $(TEST_COMPOSE_FILE) down

.PHONY: test-logs
test-logs: ## Follow logs of Docker containers for testing
	$(DC) -f $(TEST_COMPOSE_FILE) logs -f

.PHONY: test-run
test-run: ## Run tests
	$(DC) -f $(TEST_COMPOSE_FILE) down --volumes --remove-orphans
	$(DC) -f $(TEST_COMPOSE_FILE) build
	$(DC) -f $(TEST_COMPOSE_FILE) up -d
	sleep 0.1
	$(DC) -f $(TEST_COMPOSE_FILE) run backend pytest
	$(DC) -f $(TEST_COMPOSE_FILE) down --volumes --remove-orphans

.PHONY: test-run-debug
test-run-debug: ## Run tests
	$(DC) -f $(TEST_COMPOSE_FILE) down --volumes --remove-orphans
	$(DC) -f $(TEST_COMPOSE_FILE) build
	$(DC) -f $(TEST_COMPOSE_FILE) up -d
	sleep 0.1
	$(DC) -f $(TEST_COMPOSE_FILE) run backend pytest --log-cli-level=DEBUG
	$(DC) -f $(TEST_COMPOSE_FILE) down --volumes --remove-orphans

.PHONY: test-shell
test-shell: ## Open a Django shell for testing
	$(DC) -f $(TEST_COMPOSE_FILE) run backend python manage.py shell

.PHONY: test-clean
test-clean: ## Clean up Docker containers, images, and volumes for testing
	$(DC) -f $(TEST_COMPOSE_FILE) down -v --rmi all --remove-orphans

# Production targets
.PHONY: prod-build
prod-build: ## Build the Docker images for production
	$(DC) -f $(PROD_COMPOSE_FILE) build

.PHONY: prod-up
prod-up: ## Start the Docker containers for production
	$(DC) -f $(PROD_COMPOSE_FILE) up -d

.PHONY: prod-down
prod-down: ## Stop the Docker containers for production
	$(DC) -f $(PROD_COMPOSE_FILE) down

.PHONY: prod-logs
prod-logs: ## Follow logs of Docker containers for production
	$(DC) -f $(PROD_COMPOSE_FILE) logs -f

.PHONY: prod-migrate
prod-migrate: ## Run database migrations for production
	$(DC) -f $(PROD_COMPOSE_FILE) run backend python manage.py migrate

.PHONY: prod-createsuperuser
prod-createsuperuser: ## Create a superuser for production
	$(DC) -f $(PROD_COMPOSE_FILE) run backend python manage.py createsuperuser

.PHONY: prod-shell
prod-shell: ## Open a Django shell for production
	$(DC) -f $(PROD_COMPOSE_FILE) run backend python manage.py shell

.PHONY: prod-clean
prod-clean: ## Clean up Docker containers, images, and volumes for production
	$(DC) -f $(PROD_COMPOSE_FILE) down -v --rmi all --remove-orphans

# Monitoring targets
.PHONY: monitoring-build
monitoring-build: ## Build the Docker images for monitoring
	$(DC) -f $(MONITORING_COMPOSE_FILE) build

.PHONY: monitoring-up
monitoring-up: ## Start the Docker containers for monitoring
	$(DC) -f $(MONITORING_COMPOSE_FILE) up -d

.PHONY: monitoring-down
monitoring-down: ## Stop the Docker containers for monitoring
	$(DC) -f $(MONITORING_COMPOSE_FILE) down

.PHONY: monitoring-logs
monitoring-logs: ## Follow logs of Docker containers for monitoring
	$(DC) -f $(MONITORING_COMPOSE_FILE) logs -f

.PHONY: monitoring-clean
monitoring-clean: ## Clean up Docker containers, images, and volumes for monitoring
	$(DC) -f $(MONITORING_COMPOSE_FILE) down -v --rmi all --remove-orphans
