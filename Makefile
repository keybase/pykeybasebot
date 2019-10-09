.PHONY: test types clean
PROTOCOL_PATH=$(GOPATH)/src/github.com/keybase/client/protocol
AVDLC=$(PROTOCOL_PATH)/node_modules/.bin/avdlc

test:
	poetry run mypy pykeybasebot/
	poetry run python -m pytest
	poetry run flake8
	poetry run isort -rc . --check-only
	poetry run black . --check

types:
	@mkdir -p pykeybasebot/types/{keybase1,gregor1,chat1,stellar1}/
	$(AVDLC) -b -l python -t -o pykeybasebot/types/keybase1 $(PROTOCOL_PATH)/avdl/keybase1/*.avdl
	$(AVDLC) -b -l python -t -o pykeybasebot/types/gregor1 $(PROTOCOL_PATH)/avdl/gregor1/*.avdl
	$(AVDLC) -b -l python -t -o pykeybasebot/types/chat1 $(PROTOCOL_PATH)/avdl/chat1/*.avdl
	$(AVDLC) -b -l python -t -o pykeybasebot/types/stellar1 $(PROTOCOL_PATH)/avdl/stellar1/*.avdl
	poetry run black pykeybasebot/types
	poetry run isort pykeybasebot/types/**/*.py

clean:
	rm -rf src/types/*
