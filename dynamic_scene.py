from manim import *

class DynamicText(Scene):
    def construct(self):
        text = "Hello Manim, this is automated!"  # Placeholder for dynamic input
        text_obj = Text(text)
        self.play(Write(text_obj))
        self.wait(2)