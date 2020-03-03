from manimlib.imports import *

import os
import pyclbr


class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT*2)
        circle.next_to(square, DOWN, 2)

        self.play(FadeIn(square))
        self.play(Rotating(square), FadeIn(circle))


class AddingText(Scene):
    def construct(self):
        my_first_text = TextMobject("Writing with manim is fun")
        second_line = TextMobject("and easy to do!")
        second_line.next_to(my_first_text, DOWN)
        third_line = TextMobject("for me and you!")
        third_line.next_to(my_first_text, DOWN)

        self.add(my_first_text, second_line)
        self.wait()
        self.play(Transform(second_line, third_line))
        self.wait(2)
        self.play(ApplyMethod(second_line.shift, 3*DOWN))
        self.play(ApplyMethod(my_first_text.shift, 3*UP))
        self.wait()


class AddingMoreText(Scene):
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject(
            "A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        quote2.to_edge(UP)
        author = TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT) + LEFT*0.5, DOWN)

        self.add(quote)
        self.add(author)
        self.wait()
        self.play(Transform(quote, quote2), ApplyMethod(
            author.next_to, quote2.get_corner(DOWN+RIGHT) + LEFT*0.5, DOWN))
        self.wait(5)


class RotateAndHighlight(Scene):
    def construct(self):
        square = Square(side_length=5, fill_color=YELLOW, fill_opacity=1)
        label = TextMobject("Text at an angle")
        label.bg = BackgroundRectangle(label, fill_opacity=1)
        label_group = VGroup(label.bg, label)  # Order matters
        label_group.rotate(TAU/8)
        label2 = TextMobject("Boxed text", color=BLACK)
        label2.bg = SurroundingRectangle(
            label2, color=BLUE, fill_color=RED, fill_opacity=.5)
        label2_group = VGroup(label2, label2.bg)
        label2_group.next_to(label_group, DOWN)
        label2.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.wait(5)


class BasicEquations(Scene):
    def construct(self):
        eq1 = TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2 = TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait(5)


class ColoringEquations(Scene):
    def construct(self):
        line1 = TexMobject(r"\text{The vector } \vec{F}_{net} \text{ is the net }",
                           r"\text{force }", r"\text{on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2 = TexMobject(
            "m", "\\text{ and acceleration }", "\\vec{a}", ".  ")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        sentence = VGroup(line1, line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))
        self.wait(5)


class UsingBraces(Scene):
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x -2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A, RIGHT)
        eq1C.next_to(eq1B, RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A, LEFT)
        eq2B.align_to(eq1B, LEFT)
        eq2C.align_to(eq1C, LEFT)

        eq_group = VGroup(eq1A, eq2A)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces))
        self.play(GrowFromCenter(braces), Write(eq_text))
        self.wait(5)
