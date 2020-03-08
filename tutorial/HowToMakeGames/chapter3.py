from manimlib.imports import *
from gametutorialslib.imports import *

import os
import pyclbr


class ExamplesOfVectors(DefaultThreeDScene):
    def construct(self):
        vec_text_start = TextMobject("(2, 3, 2)")
        self.add(vec_text_start)
        self.wait(2)

        vec_text = vec_text_start.copy()
        vec_arrow = Arrow(ORIGIN, RIGHT)

        vec_axes = DefaultThreeDAxes()
        self.mobject_face_default_perspective(vec_axes)
        vec_group = VGroup(vec_text, vec_arrow, vec_axes)
        vec_group.arrange_submobjects(RIGHT)
        vec_group.to_edge(LEFT+UP, LARGE_BUFF)
        vec_axes.next_to(vec_arrow, RIGHT*1.5, LARGE_BUFF)
        vec_group.shift(RIGHT)

        x_label, z_label, y_label = vec_axes.get_axis_labels("x", "z", "y")

        point_coord = [2, 2, 3]
        point = Dot(vec_axes.coords_to_point(*point_coord), color=YELLOW)
        point_label = vec_text.copy().scale(0.7)
        point_label.next_to(point).set_color(point.get_color())

        local_stroke_width = DEFAULT_STROKE_WIDTH*1.5
        x_line = Line(vec_axes.coords_to_point(0, 0, 0),
                      vec_axes.coords_to_point(point_coord[0]), color=RED_D, stroke_width=local_stroke_width)

        y_line = Line(vec_axes.coords_to_point(point_coord[0]), vec_axes.coords_to_point(
            point_coord[0], 0, point_coord[2]), color=GREEN_D, stroke_width=local_stroke_width)

        z_line = Line(vec_axes.coords_to_point(point_coord[0], 0, point_coord[2]), vec_axes.coords_to_point(
            *point_coord), color=BLUE_D, stroke_width=local_stroke_width)

        x_number_label = TextMobject("2")
        x_number_label.scale(0.7).next_to(
            x_line, DOWN, SMALL_BUFF).set_color(x_line.get_color())

        y_number_label = TextMobject("3")
        y_number_label.scale(0.7).next_to(
            y_line, RIGHT, SMALL_BUFF).shift(DOWN*0.15).set_color(y_line.get_color())

        z_number_label = TextMobject("2")
        z_number_label.scale(0.7).next_to(
            z_line, UP, SMALL_BUFF).set_color(z_line.get_color())

        self.play(Transform(vec_text_start, vec_text), FadeIn(vec_arrow),
                  GrowFromCenter(VGroup(vec_axes, x_label, z_label, y_label)))
        self.remove(vec_text_start)
        self.add(vec_text)

        self.wait(2)

        self.play(ShowCreation(x_line), FadeIn(x_number_label))
        self.play(ShowCreation(y_line), FadeIn(y_number_label))
        self.play(ShowCreation(z_line), FadeIn(z_number_label),
                  FadeIn(VGroup(point, point_label)))

        self.wait(2)

        ######################

        fade_out_group = VGroup(x_line, z_line, y_line, x_number_label,
                                y_number_label, z_number_label, point)
        vec_dir = Line(vec_axes.coords_to_point(0, 0, 0), vec_axes.coords_to_point(
            *point_coord), color=point.get_color())
        vec_dir.add_tip(.2)

        self.play(FadeOut(fade_out_group))
        self.play(ShowCreation(vec_dir))
        self.wait(2)

        ##################

        color_text = TextMobject("(207, 29, 198)").move_to(vec_text)
        color_arrow = vec_arrow.copy()
        color_arrow.next_to(color_text, RIGHT)
        square_color = Square(color="#cf1dc6", fill_opacity=1)
        square_color.move_to(vec_axes)

        self.play(Transform(vec_arrow, color_arrow), Transform(vec_text, color_text), Transform(VGroup(vec_axes, vec_dir), square_color),
                  FadeOut(VGroup(x_label, z_label, y_label, point_label)))

        self.wait(5)


class UnityAxesTransparent(DefaultThreeDScene):
    def construct(self):
        local_scale = 2.5
        unity_axes = UnityAxes()
        self.mobject_face_default_perspective(unity_axes)
        unity_axes.scale(local_scale)

        x_line, x_tip = unity_axes.create_line_and_tip_from_axis(0)
        z_line, z_tip = unity_axes.create_line_and_tip_from_axis(1)
        y_line, y_tip = unity_axes.create_line_and_tip_from_axis(2)

        x_label = unity_axes.get_x_axis_label(
            "x", buff=0.75).scale(local_scale*0.8)
        z_label = unity_axes.get_y_axis_label(
            "z", buff=MED_LARGE_BUFF).scale(local_scale)
        y_label = unity_axes.get_z_axis_label(
            "y", buff=0.75).scale(local_scale*0.8)

        x_line.set_stroke(width=10)
        y_line.set_stroke(width=10)
        z_line.set_stroke(width=10)

        self.add(VGroup(y_line, y_tip, y_label))
        self.wait()
        self.add(VGroup(x_line, x_tip, x_label))
        self.wait()
        self.add(VGroup(z_line, z_tip, z_label))
        self.wait()


class VectorsAsDirection(DefaultThreeDScene):
    def construct(self):
        vec_axes = UnityAxes()
        self.mobject_face_default_perspective(vec_axes)
        vec_axes.center()
        # vec_axes.shift(RIGHT*2)

        x_label, z_label, y_label = vec_axes.get_axis_labels("x", "z", "y")

        vec_group = VGroup(vec_axes, x_label, z_label, y_label)

        self.wait(0.5)
        self.play(ShowCreation(vec_group))
        self.wait(2)
        point_coord = [5, 10, 2]
        vec_text = TextMobject("(5, 2, 10)")
        vec_dir = Line(vec_axes.coords_to_point(0, 0, 0), vec_axes.coords_to_point(
            *point_coord), color=WHITE)
        vec_dir.add_tip(.2)

        vec_text.next_to(vec_dir.get_tip(), RIGHT+UP)

        self.play(ShowCreation(vec_text))
        self.wait(2)
        self.play(ShowCreation(vec_dir))
        self.wait(2)

        point = Dot(vec_axes.coords_to_point(
            0, 0, 0), color=YELLOW, radius=0.15)
        self.play(GrowFromCenter(point))

        local_stroke_width = DEFAULT_STROKE_WIDTH*3
        x_line = Line(vec_axes.coords_to_point(0, 0, 0),
                      vec_axes.coords_to_point(point_coord[0]), color=UNITY_X_COLOR, stroke_width=local_stroke_width)

        y_line = Line(vec_axes.coords_to_point(point_coord[0]), vec_axes.coords_to_point(
            point_coord[0], 0, point_coord[2]), color=UNITY_Z_COLOR, stroke_width=local_stroke_width)

        z_line = Line(vec_axes.coords_to_point(point_coord[0], 0, point_coord[2]), vec_axes.coords_to_point(
            *point_coord), color=UNITY_Y_COLOR, stroke_width=local_stroke_width)

        self.play(ShowCreation(x_line), ApplyMethod(
            point.move_to, x_line.get_end()))
        self.play(ShowCreation(y_line), ApplyMethod(
            point.move_to, y_line.get_end()))
        self.play(ShowCreation(z_line), ApplyMethod(
            point.move_to, z_line.get_end()))

        self.wait(5)
