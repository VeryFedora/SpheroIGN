import sys
sys.coinit_flags = 0
import asyncio 
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import pygame
import spherov2
# Can't believe i have to add this, garbage language.
class GlobalVariable:
    val = None;
    def __init__(self, val):
        self.val = val;
    def set(self, val):
        self.val = val;
    def get(self):
        return self.val;


running = GlobalVariable(True);