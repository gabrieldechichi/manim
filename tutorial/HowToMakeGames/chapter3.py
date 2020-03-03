from manimlib.imports import *

import os
import pyclbr


class DefaultThreeDAxes(ThreeDAxes):
    CONFIG = {
        "shade_in_3d": True,
        "number_line_config": {
            "include_ticks": True,
            "unit_size": .5,
        },
        "x_axis_config": {
            "x_min": -2,
            "x_max": 10
        },
        "y_axis_config": {
            "x_min": -2,
            "x_max": 10
        },
        "z_axis_config": {
            "x_min": -2,
            "x_max": 10
        },
    }

    def get_axis_label(self, label_tex, axis, edge, direction, buff=MED_SMALL_BUFF):
        tip = axis.get_tip()
        label_pos = tip.get_tip_point() - tip.get_vector() * \
            axis.unit_size + direction*buff
        label = TexMobject(label_tex)
        label.set_color(axis.get_color())
        label.move_to(label_pos)
        return label

    def get_z_axis_label(self, label_tex, edge=UP, direction=RIGHT, **kwargs):
        return self.get_axis_label(
            label_tex, self.get_z_axis(),
            edge, direction, **kwargs
        )

    def get_axis_labels(self, x_label_tex="x", y_label_tex="y", z_label_tex="z"):
        self.axis_labels = VGroup(
            self.get_x_axis_label(x_label_tex),
            self.get_y_axis_label(y_label_tex),
            self.get_z_axis_label(z_label_tex)
        )
        return self.axis_labels

    def create_line_and_tip_from_axis(self, index):
        axis = self.get_axis(index)
        tip = axis.get_tip().copy()
        line = Line(axis.get_start(), axis.get_end() - tip.get_vector()
                    ).set_color(axis.get_color())
        return [line, tip]


UNITY_X_COLOR = "#bc2e18"
UNITY_Y_COLOR = "#438bf1"
UNITY_Z_COLOR = "#7ed13a"


class UnityAxes(DefaultThreeDAxes):
    CONFIG = {
        "shade_in_3d": True,
        "number_line_config": {
            "include_ticks": True,
            "unit_size": .5,
        },
        "x_axis_config": {
            "color": UNITY_X_COLOR,
            "x_min": -2,
            "x_max": 10
        },
        "z_axis_config": {
            "color": UNITY_Z_COLOR,
            "x_min": -2,
            "x_max": 10
        },
        "y_axis_config": {
            "color": UNITY_Y_COLOR,
            "x_min": -2,
            "x_max": 10
        }
    }


class DefaultThreeDScene(ThreeDScene):
    CONFIG = {
        "default_perspective_angles": {
            "phi": 60*DEGREES,
            "theta": -45 * DEGREES,
            "gamma": 0
        }
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        ThreeDScene.__init__(self, **kwargs)

    def mobject_face_camera(self, obj):
        face_camera_matrix = np.linalg.inv(self.camera.get_rotation_matrix())
        obj.apply_points_function_about_point(
            lambda points: np.dot(points, face_camera_matrix.T)
        )

    def mobject_face_default_perspective(self, obj):
        temp_cam = ThreeDCamera(**self.default_perspective_angles)
        face_camera_matrix = temp_cam.get_rotation_matrix()
        obj.apply_points_function_about_point(
            lambda points: np.dot(points, face_camera_matrix.T)
        )


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


class Test(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(
            theta=-45 * DEGREES, phi=60*DEGREES)
        plane = UnityAxes_ExamplesOfVectors(
            number_line_config={"include_ticks": True, "include_tip": True},
            x_axis_config={"x_min": 0, "x_max": 5},
            y_axis_config={"x_min": 0, "x_max": 5},
            z_axis_config={"x_min": 0, "x_max": 5})

        # plane.rotate(-40*DEGREES, UP,
        #              about_point=plane.get_y_axis().get_start())
        x_label, y_label = plane.get_axis_labels().split()
        planeGroup = VGroup(plane, x_label, y_label)
        self.play(ShowCreation(planeGroup))
        self.show_vector_coordinates()

        self.wait(5)

    def show_vector_coordinates(self):
        starting_mobjects = list(self.mobjects)

        vectorX, vectorY = [3, 2]
        vector = Vector([vectorX, vectorY])
        x_line = Line(ORIGIN, vectorX*RIGHT)
        y_line = Line(vectorX*RIGHT, vectorX*RIGHT+vectorY*UP)
        x_line.set_color(X_COLOR)
        y_line.set_color(Y_COLOR)

        x_label = TextMobject("3", color=x_line.get_color())
        x_label.next_to(x_line, DOWN)
        y_label = TextMobject("2", color=y_line.get_color())
        y_label.next_to(y_line, RIGHT)

        point = Dot(vectorX*RIGHT+vectorY*UP, radius=0.1)

        self.play(FadeIn(point))
        self.play(
            FadeIn(x_label),
            ShowCreation(x_line),
            FadeIn(y_label),
            ShowCreation(y_line),
        )

        self.bring_to_front(point)


class HowIWantYouToThinkAboutVectors(Scene):
    def construct(self):
        vector = Vector([-2, 3])
        plane = NumberPlane()
        axis_labels = plane.get_axis_labels()
        tempVectors = map(Vector, [[1, 2], [2, -1], [4, 0]])
        other_vectors = VGroup(*list(tempVectors))
        colors = [GREEN_B, MAROON_B, PINK]
        for v, color in zip(other_vectors.split(), colors):
            v.set_color(color)
        shift_val = 4*RIGHT+DOWN

        dot = Dot(radius=0.1)
        dot.set_color(RED)
        tail_word = TextMobject("Tail")
        tail_word.shift(0.5*DOWN+2.5*LEFT)
        line = Line(tail_word, dot)

        self.play(ShowCreation(vector))
        self.wait(2)
        self.play(
            ShowCreation(plane, lag_ratio=0.5),
            Animation(vector)
        )
        self.play(Write(axis_labels, run_time=1))
        self.wait()
        self.play(
            GrowFromCenter(dot),
            ShowCreation(line),
            Write(tail_word, run_time=1)
        )
        self.wait()
        self.play(
            FadeOut(tail_word),
            ApplyMethod(VGroup(dot, line).scale, 0.01)
        )
        self.remove(tail_word, line, dot)
        self.wait()

        self.play(ApplyMethod(
            vector.shift, shift_val,
            path_arc=3*np.pi/2,
            run_time=3
        ))
        self.play(ApplyMethod(
            vector.shift, -shift_val,
            rate_func=rush_into,
            run_time=0.5
        ))
        self.wait(3)

        self.play(ShowCreation(
            other_vectors,
            run_time=3
        ))
        self.wait(3)

        x_axis, y_axis = plane.get_axes().split()
        x_label = axis_labels.split()[0]
        x_axis = x_axis.copy()
        x_label = x_label.copy()
        everything = VGroup(*self.mobjects)
        self.play(
            FadeOut(everything),
            Animation(x_axis), Animation(x_label)
        )


class CoordinateSystemWalkthrough(VectorScene):
    def construct(self):
        # self.introduce_coordinate_plane()
        self.show_vector_coordinates()
        # self.coords_to_vector([3, -1])
        # self.vector_to_coords([-2, -1.5], integer_labels=False)

    def introduce_coordinate_plane(self):
        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        x_label, y_label = plane.get_axis_labels().split()
        number_line = NumberLine(tick_frequency=1)
        x_tick_marks = number_line.get_tick_marks()
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)
        tick_marks = VGroup(x_tick_marks, y_tick_marks)
        tick_marks.set_color(WHITE)
        plane_lines = [m for m in plane.get_family() if isinstance(m, Line)]
        origin_words = TextMobject("Origin")
        origin_words.shift(2*UP+2*LEFT)
        dot = Dot(radius=0.1).set_color(RED)
        line = Line(origin_words.get_bottom(), dot.get_corner(UP+LEFT))

        unit_brace = Brace(Line(RIGHT, 2*RIGHT))
        one = TexMobject("1").next_to(unit_brace, DOWN)

        self.add(x_axis, x_label)
        self.wait()
        self.play(ShowCreation(y_axis))
        self.play(Write(y_label, run_time=1))
        self.wait(2)
        self.play(
            Write(origin_words),
            GrowFromCenter(dot),
            ShowCreation(line),
            run_time=1
        )
        self.wait(2)
        self.play(
            FadeOut(VGroup(origin_words, dot, line))
        )
        self.remove(origin_words, dot, line)
        self.wait()
        self.play(
            ShowCreation(tick_marks)
        )
        self.play(
            GrowFromCenter(unit_brace),
            Write(one, run_time=1)
        )
        self.wait(2)
        self.remove(unit_brace, one)
        self.play(
            *list(map(GrowFromCenter, plane_lines)) + [
                Animation(x_axis), Animation(y_axis)
            ])
        self.wait()
        self.play(
            FadeOut(plane),
            Animation(VGroup(x_axis, y_axis, tick_marks))
        )
        self.remove(plane)
        self.add(tick_marks)

    def show_vector_coordinates(self):
        starting_mobjects = list(self.mobjects)

        vector = Vector([-2, 3])
        x_line = Line(ORIGIN, -2*RIGHT)
        y_line = Line(-2*RIGHT, -2*RIGHT+3*UP)
        x_line.set_color(X_COLOR)
        y_line.set_color(Y_COLOR)

        array = vector_coordinate_label(vector)
        x_label, y_label = array.get_mob_matrix().flatten()
        x_label_copy = x_label.copy()
        x_label_copy.set_color(X_COLOR)
        y_label_copy = y_label.copy()
        y_label_copy.set_color(Y_COLOR)

        point = Dot(4*LEFT+2*UP)
        point_word = TextMobject("(-4, 2) as \\\\ a point")
        point_word.scale(0.7)
        point_word.next_to(point, DOWN)
        point.add(point_word)

        self.play(ShowCreation(vector))
        self.play(Write(array))
        self.wait(2)
        self.play(ApplyMethod(x_label_copy.next_to, x_line, DOWN))
        self.play(ShowCreation(x_line))
        self.wait(2)
        self.play(ApplyMethod(y_label_copy.next_to, y_line, LEFT))
        self.play(ShowCreation(y_line))
        self.wait(2)
        self.play(FadeIn(point))
        self.wait()
        self.play(ApplyFunction(
            lambda m: m.scale_in_place(1.25).set_color(YELLOW),
            array.get_brackets(),
            rate_func=there_and_back
        ))
        self.wait()
        self.play(FadeOut(point))
        self.remove(point)
        self.wait()
        self.clear()
        self.add(*starting_mobjects)
