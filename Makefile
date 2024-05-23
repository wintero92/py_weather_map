SHELL := /bin/bash

COVERAGE_INT := 97

test.int:
	source .venv/bin/activate && \
	coverage run \
		--branch \
		--source=weather_map \
		--module pytest \
		--capture=no test/int && \
	coverage html --directory=coverage/int && \
	coverage report --show-missing --fail-under=$(COVERAGE_INT)