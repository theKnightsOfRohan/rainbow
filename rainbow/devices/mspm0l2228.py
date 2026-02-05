# This file is created for use in ectf2026 by UIUC SIGPwny.
# Use at your own risk.

import random
import pickle
import importlib.resources

import unicorn as uc

from ..generics import rainbow_cortexm
from ..utils import parse_svd


class rainbow_mspm0(rainbow_cortexm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _load_other_regs(self, filename):
        """
        Load OTHER_REGS from a dictionary in a pickle file.
        :param filename: pickle file path.
        """
        with open(filename, 'rb') as f:
            self.OTHER_REGS = parse_svd.parse_svd(f)

class rainbow_mpsm0l2228(rainbow_mspm0):
    FLASH = (0x00006000, 0x00039FFF)
    RAM = (0x20200000, 0x20207FFF)
    FSMC = (0x00800000, 0x0083FFFF)
    PERIPHERALS = (0x40000000, 0x40FFFFFF)
    INTERNAL = (0xE0000000, 0xE00FFFFF)
    STACK_ADDR = RAM[1]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load register dictionary dumped from SVD file
        with importlib.resources.path(__package__, "MSPM0L222X.svd") as regs_svd:
            self._load_other_regs(regs_svd)

        # Map specific memory regions
        self.map_space(*self.FLASH)
        self.map_space(*self.RAM)
        self.map_space(*self.FSMC)
        self.map_space(*self.PERIPHERALS)
        self.map_space(*self.INTERNAL)
