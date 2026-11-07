.PHONY: test install clean demo bench docker

install:
	pip install -e .[test]

test:
	pytest tests/ -q

demo:
	python examples/modes_demo.py

bench:
	python examples/benchmark.py

docker:
	docker build -t quantumarmor .
	docker run --rm quantumarmor

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache dist build *.egg-info
