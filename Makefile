SHELL := /bin/bash

COVERAGE_UNIT := 0

test.unit:
	source .venv/bin/activate && \
	coverage run \
		--branch \
		--source=weather_map \
		--module pytest \
		--capture=no test/unit && \
	coverage html --directory=coverage/unit && \
	coverage report --show-missing --fail-under=$(COVERAGE_UNIT)