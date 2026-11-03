.PHONY: test install clean demo

install:
	pip install -e .[test]

test:
	pytest tests/ -q

demo:
	python examples/modes_demo.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache dist build *.egg-info
