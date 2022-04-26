.DEFAULT_GOAL := help

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

requirements: ## install development environment requirements
	pip install -r requirements.txt --exists-action w

serve:  ## Start the development server
	python manage.py runserver 0.0.0.0:8000

migrate: ## Run migrations
	python manage.py migrate

start_dev_server: requirements migrate serve  ## Setup and start the development server

.PHONY: requirements help serve migrate start_dev_server
