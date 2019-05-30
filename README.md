# Python Keybase Bot Library

This is an unopinionated, simple wrapper around the Keybase CLI API for creating an interactive bot or general scripting. This library does not attempt to do intent parsing or manage state at all. You'll have to build that yourself, but with the examples, this library will hopefully make whatever you want to build much much easier `:)`.

See https://github.com/keybase/keybase-bot for a similar framework in Javascript.

This library is very far from exhaustively covering the complete Keybase API, but it is our hope that it will be easy to add to (see chat_client.py for the pattern). It currently does reading from channels and writing messages/reactions pretty well. That's enough for the vast majority of basic functionality. Future work can add teams behavior, more wallet functionality (e.g. sending money), ...


## Installation
Python 3.6 or greater, please. And it's all async, so you'll need to call into it with that in mind.

## Examples
Yeah. Check out the examples. There are some docs, but we're really counting on the examples to make this all usable.
