# !/usr/bin/env python3
# aes128 from https://github.com/Ko-/aes-armcortexm

from binascii import hexlify

import lascar
import numpy as np
from lascar.tools.aes import sbox
from rainbow.generics import rainbow_arm
from rainbow import TraceConfig, HammingWeight
from visplot import plot

e = rainbow_arm(trace_config=TraceConfig(register=HammingWeight()))
e.load("hsm.elf", typ=".elf")
e.setup()

e.start(0x00006000)
print(e.trace)
