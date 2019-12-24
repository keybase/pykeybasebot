# pykeybasebot

[![PyPI](https://img.shields.io/pypi/v/pykeybasebot)](https://pypi.org/project/pykeybasebot/) [![Build Status](https://travis-ci.com/keybase/pykeybasebot.svg?branch=master)](https://travis-ci.com/keybase/pykeybasebot)

This is the officially support Keybase Python library. It is an unopinionated, simple wrapper around the Keybase CLI API for creating an interactive bot or general scripting. This library does not attempt to do intent parsing or manage state at all. You'll have to build that yourself, but with the examples, this library will hopefully make whatever you want to build much much easier `:)`.

There are also similar libraries for [JavaScript](https://github.com/keybase/keybase-bot) and [Go](https://github.com/keybase/go-keybase-chat-bot).

This library is very far from exhaustively covering the complete Keybase API, but it is our hope that it will be easy to add to (see chat_client.py for the pattern). It currently does reading from channels and writing messages/reactions pretty well. That's enough for the vast majority of basic functionality. Future work can add teams behavior, more wallet functionality (e.g. sending money), ...

## Installation

```
pip install pykeybasebot
```

Python 3.7 or greater, please. And it's all async, so you'll need to call into it with that in mind.

## Setup

Generally speaking, here's what you need to do:

1. Create a handler function that takes event objects and does something with them. This function will get called with your bot instance (described below) and the KbEvent instance.
2. Create a bot. You _must_ initialize this with the handler function to call with each event. You _may_ optionally pass in: (1) the username and/or paperkey for the bot's identity (it'll default to the currently logged-in user otherwise), (1) the event loop that you want new tasks to be sent to (this is necessary if you want to lock on async behavior -- see the examples), (2) the location of the running keybase app (defaults to `keybase` which is fine if it's in your PATH), your user's home directory, or pid_file. These three are more useful for complicated local development with multiple accounts and less useful if you're running in a docker container or as the only user on your system.
3. If you are not already running on a logged-in device, you need to do that. We recommend doing this with the `oneshot` command. It's in the examples.
4. start the bot inside the asyncio event loop. This bot command wraps `keybase chat api-listen`, (and it takes basically the same exact options) and fires off events to your handler function.

## Examples

Definitely definitely check out the examples. We're really counting on them to make it clear how to use this library.

## Contributing

PRs are extremely welcome. To start:

```
git clone https://github.com/keybase/pykeybasebot
cd pykeybasebot
```

We use [Poetry](https://poetry.eustace.io/) to handle our packaging. Go check out their website for installation instructions. To start Poetry, you'll need the `python` executable in your path to link to Python 3.7. We recommend using [pyenv](https://github.com/pyenv/pyenv) to handle different versions of Python on your machine. With pyenv installed, it should automatically set `python` to 3.7 when you `cd` into this repo.

Once you have the right Python version, you can run:

```
pip install poetry
poetry install
```

This will set up a virtualenv for you and install all the dependencies needed into it!

Remember that if you're making changes to pykeybasebot and want to test them
locally, you'll need to first uninstall previously installed pykeybasebot, 
then install your local version:

```
pip uninstall pykeybasebot
poetry build
pip install ./dist/pykeybasebot-{tags}.whl
```

### Static code analysis tools

We use a few different static analysis tools to perform linting, type-checking, formatting, etc. The correct versions should be install when you run `poetry install`, but you'll probably want to configure your editor to work with:

- [mypy](http://www.mypy-lang.org/) (Type checking)
- [black](https://github.com/psf/black) (code formatting)
- [isort](https://github.com/timothycrosley/isort) (import formatting)
- [flake8](http://flake8.pycqa.org) (linting)

#### pre-commit hooks

We check all git commits with the above tools with
[pre-commit.com](http://pre-commit.com) pre-commit hooks.
To enable use of these pre-commit hooks:

- [Install](http://pre-commit.com/#install) the `pre-commit` utility.
- Remove any existing pre-commit hooks via `rm .git/hooks/pre-commit`
- Configure via `pre-commit install`

Then proceed as normal.

### Testing

To run tests, type

```
make test
```

Tests are admittedly weak. You could change that!

### Types

Most of the types the bot uses are generated from definitions defined in the [`protocol/`](https://github.com/keybase/client/tree/master/protocol) directory inside the Keybase client repo. This ensures that the types that the bot uses are consistent across bots and always up to date with the output of the API.

To build the types for the Python bot, you'll need to clone the `client` repo. This requires [Go](https://golang.org/) and your [GOPATH](https://github.com/golang/go/wiki/SettingGOPATH) to be set up.

```shell
go get github.com/keybase/client/go/keybase
```

and install the necessary dependencies for compiling the protocol files. This requires [node.js](https://nodejs.org) and [Yarn](https://yarnpkg.com).

```shell
cd client/protocol
yarn install
```

Then you can generate the types by using the provided Makefile in this repo.

```shell
cd path/to/keybase-bot
make types
```

Should you need to remove all the types for some reason, you can run `make clean`.

### Publishing

Poetry can build and publish packages to PyPI. We've run into some issues with uploading to PyPI and Poetry, though, so for now we're recommending building with Poetry and uploading with Twine.

```shell
poetry build
# Upload to Test PyPi. You only need to run the first command once
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish -r testpypi
# Upload to real PyPi
poetry publish
```
