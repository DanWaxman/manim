from big_ol_pile_of_manim_imports import *

class ControlScene(Scene):
    def contstruct(self):
        floor = Rectangle(height=1, width=14.42)
        floor.move_to(DOWN * 7.5)

        self.play(FadeIn(floor))
