.PHONY: test types clean
PROTOCOL_PATH=$(GOPATH)/src/github.com/keybase/client/protocol
AVDLC=$(PROTOCOL_PATH)/node_modules/.bin/avdlc

test-static:
	poetry run mypy pykeybasebot/
	poetry run flake8
	poetry run isort -rc . --check-only
	poetry run black . --check

test-unit:
	poetry run python -m pytest tests/unit -s

test-accept:
	poetry run python -m pytest tests -s

ci: test-static test-unit

test: test-static test-accept

types:
	@mkdir -p pykeybasebot/types/keybase1
	@mkdir -p pykeybasebot/types/gregor1
	@mkdir -p pykeybasebot/types/chat1
	@mkdir -p pykeybasebot/types/stellar1
	$(AVDLC) -b -l python -t -o pykeybasebot/types/keybase1 $(PROTOCOL_PATH)/avdl/keybase1/*.avdl
	$(AVDLC) -b -l python -t -o pykeybasebot/types/gregor1 $(PROTOCOL_PATH)/avdl/gregor1/*.avdl
	$(AVDLC) -b -l python -t -o pykeybasebot/types/chat1 $(PROTOCOL_PATH)/avdl/chat1/*.avdl
	$(AVDLC) -b -l python -t -o pykeybasebot/types/stellar1 $(PROTOCOL_PATH)/avdl/stellar1/*.avdl
	poetry run isort pykeybasebot/types/**/*.py
	poetry run black pykeybasebot/types

clean:
	rm -rf src/types/*
