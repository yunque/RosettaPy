#!/usr/bin/env python

'''Computer says it was all a dream.

Submitted to Rosetta Code @ 160920
http://rosettacode.org/wiki/Speech_synthesis#Python
'''

import pyttsx

engine = pyttsx.init()
engine.say("It was all a dream.")
engine.runAndWait()
