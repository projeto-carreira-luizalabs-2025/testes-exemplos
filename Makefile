clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.log" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f .coverage.NB-SBDEV*
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log
	@rm -f .env.bkp*

run-another:
	python another_main.py

run-api:
	uvicorn --reload app.api:app --port 5000

test:
	pytest tests

coverage:
	pytest --cov=app --cov-report=term-missing --cov-report=xml ./tests/ --cov-fail-under=90 --durations=5

coverage-no-fail:
	pytest --cov=app --cov-report=term-missing --cov-report=xml ./tests/ 
	
coverage-html:
	pytest --cov=app --cov-report=term-missing --cov-report=html ./tests/