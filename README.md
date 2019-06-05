
This is the officially support Keybase Python library. It is an unopinionated, simple wrapper around the Keybase CLI API for creating an interactive bot or general scripting. This library does not attempt to do intent parsing or manage state at all. You'll have to build that yourself, but with the examples, this library will hopefully make whatever you want to build much much easier `:)`.

See https://github.com/keybase/keybase-bot for a similar framework in Javascript.

This library is very far from exhaustively covering the complete Keybase API, but it is our hope that it will be easy to add to (see chat_client.py for the pattern). It currently does reading from channels and writing messages/reactions pretty well. That's enough for the vast majority of basic functionality. Future work can add teams behavior, more wallet functionality (e.g. sending money), ...


## Installation
```
pip install pykeybasebot
```
Python 3.7 or greater, please. And it's all async, so you'll need to call into it with that in mind.


## Setup
Generally speaking, here's what you need to do:
1. Create a handler function that takes event objects and does something with them. This function will get called with your bot instance (described below) and the KbEvent instance.
2. Create a bot. You _must_ initialize this with the username of the running keybase user and the handler function to call with each event. You _may_ optionally pass in: (1) the event loop that you want new tasks to be sent to (this is necessary if you want to lock on async behavior -- see the examples), (2) the location of the running keybase app (defaults to `keybase` which is fine if it's in your PATH), your user's home directory, or pid_file. These three are more useful for complicated local development with multiple accounts and less useful if you're running in a docker container or as the only user on your system.
3. If you are not already running on a logged-in device, you need to do that. We recommend doing this with the `oneshot` command. It's in the examples.
4. start the bot inside the asyncio event loop. This bot command wraps `keybase chat api-listen`, (and it takes basically the same exact options) and fires off events to your handler function.


## Examples
Definitely definitely check out the examples. We're really counting on them to make it clear how to use this library.


## Developing
PRs are extremely welcome. First, hop into a Python 3.7 environment however you like to manage python environments. The tests are admittedly weak. If you clone and pull down the repo, this command should get you all set up:
```
python setup.py test
```

### Updating
Increment the version in setup.py, compile the new version, and push it to PyPI.
```
python setup.py sdist bdist_wheel
python -m twine upload dist/* --verbose
```
