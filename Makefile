SHELL := /bin/bash

COVERAGE_UNIT := 100
COVERAGE_INT := 93

test.unit:
	source .venv/bin/activate && \
	coverage run \
		--branch \
		--source=weather_map \
		--module pytest \
		--capture=no test/unit && \
	coverage html --directory=coverage/unit && \
	coverage report --show-missing --fail-under=$(COVERAGE_UNIT)

test.int:
	source .venv/bin/activate && \
	coverage run \
		--branch \
		--source=weather_map \
		--module pytest \
		--capture=no test/int && \
	coverage html --directory=coverage/int && \
	coverage report --show-missing --fail-under=$(COVERAGE_INT)
