#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load("/Users/swa_isthecreator/Documents/Lambda-CS-Projects/Computer-Architecture/ls8/examples/print8.ls8")
cpu.run()