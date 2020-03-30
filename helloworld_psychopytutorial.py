"""
Demo: show a very basic program: hello world
"""

from __future__ import absolute_import, division, print_function


# Import key parts of the PsychoPy library:
from psychopy import visual, core

# Create a visual window:
win = visual.Window()

# Create (but not yet display) some text:
msg1 = visual.TextStim(win, text=u"Hello world!")  # default position = centered
msg2 = visual.TextStim(win, text=u"\u00A1Hola mundo!", pos=(0, -0.3))

# Now I'm adding code to display the current date and time

msg3 = visual.TextStim(win, text=u"Current date and time : ")
msg4 = visual.TextStim(win, text=now.strftime("%Y=%m-%d %H:%M:%S"))


# Draw the text to the hidden visual buffer:
msg1.draw()
msg2.draw()
msg3.draw()
msg4.draw()

# Show the hidden buffer--everything that has been drawn since the last win.flip():
win.flip()

# Wait 3 seconds so people can see the message, then exit gracefully:
# Changed from 3 seconds to 30
core.wait(30)

win.close()
core.quit()

# The contents of this file are in the public domain.

