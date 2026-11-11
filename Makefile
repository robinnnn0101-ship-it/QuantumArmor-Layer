.PHONY: test demo benchmark v07 clean install

install:
	pip install -e .

test:
	python -m pytest tests/ -q

demo:
	python examples/03_full_demo.py

benchmark:
	python examples/benchmark.py

v07:
	python examples/v07_demo.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
