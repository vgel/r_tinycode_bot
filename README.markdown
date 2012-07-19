[/r/tinycode](http://www.reddit.com/r/tinycode) submission tracking bot
=======================================================================

This bot tracks submissions in the /r/tinycode new queue and generates language data about them.

The bot uses several hueristics to try and identify files:

* A tag on the title specifying it's language ([Python] Coolio)
* Language names in the title (Coolio, a tiny Python program)
* Shebang lines
* File extensions

The bot's files are:
* bot_visted - a plaintext file containing submission ids the bot has visited