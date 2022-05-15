# corekeeper-fishing-bot
a very simple fishing bot for Core Keeper written in python


## Disclaimer

The computer could have some performance issues, while running the bot, because it captures the screen multiple times per second.
Yes, it captures your screen partially. But the screenshots are only created temporarily, so you don't have to worry about abuse of it.


## Some information

The Core Keeper window has to be fullscreen on the main screen!
I tested it with 1920x1080 and 2560x1440. Smaller screens could possibly lead to problems.

The bot doesn't see if a fish is biting, it waits for a certain time until it reels in the fishing rod so it catches not alway something. This time is optimated for the skill 'improved bait'.
I recommend using the scarlet fishing rod and the sea foam rings for high fishing too, but I am not sure what is affected by it.

You shouldn't place your cursor on top of the minigame or the caught-message (the corners of the screen aren't recommend too as they trigger the fail-save).
And you should make sure enemies can't kill you while beeing afk. ;)


## How to use it

1. Download the .py-File. You have to install python, if it is not already installed and the necessary libraries.
  * Python: https://www.python.org/downloads/
  * Pip: https://pypi.org/project/pip/#files
  * execute ```pip install keyboard pyautogui pillow```
3. Execute the file.
4. Start the bot with holding the shift key for 5 seconds.
5. Lean back.


## Controls

* shift     - start/unpause (hold the key for 5 seconds down)
* p         - pause
* x         - stop

fail-save   - moving your mouse to a corner of the screen
