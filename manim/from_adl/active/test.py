#!/usr/bin/env python

from manimlib.imports import *

class test(Scene):
    def construct(self):
        title=TextMobject("This is a test")
        dot=Dot()
        dot.to_edge(DOWN)

        self.play(Write(title))
        self.wait()

        self.add(dot)
        self.wait()

        dot.to_edge(UP)
        self.add(dot)
        self.wait()

        dot.to_corner(UL) #DR, DL, UR => Down Right, Down Left, Up Right, etc.
        self.add(dot)
        self.wait()