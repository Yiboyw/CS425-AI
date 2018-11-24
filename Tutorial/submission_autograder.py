# submission_autograder.py
# ------------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from codecs import open

"""
CS 188 Local Submission Autograder
Written by the CS 188 Staff

==============================================================================
   _____ _              _ 
  / ____| |            | |
 | (___ | |_ ___  _ __ | |
  \___ \| __/ _ \| '_ \| |
  ____) | || (_) | |_) |_|
 |_____/ \__\___/| .__/(_)
                 | |      
                 |_|      

Modifying or tampering with this file is a violation of course policy.
If you're having trouble running the autograder, please contact the staff.
==============================================================================
"""
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))


