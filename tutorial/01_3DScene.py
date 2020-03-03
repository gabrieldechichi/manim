from manimlib.imports import *

import os
import pyclbr


class UnityAxes(ThreeDAxes):
    CONFIG = {
        "shade_in_3d": True,
        "number_line_config": {
            "include_ticks": False,
        },
        "x_axis_config": {
            "color": "#bc2e18",
            "x_min": 0,
            "x_max": 2
        },
        "z_axis_config": {
            "color": "#7ed13a",
            "x_min": 0,
            "x_max": 2
        },
        "y_axis_config": {
            "color": "#438bf1",
            "x_min": 0,
            "x_max": 2
        }
    }


class ThreeDSceneCube(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "should_apply_shading": True,
            "exponential_projection": True
        }
    }

    def construct(self):
        # camera orientation is in polar coordinates
        # theta = XY angle, phi = 3D angle, distance = 3, gamma = Rotate around it's own axis
        # default orientation is phi = 0, theta = -PI/2
        # self.set_camera_orientation(
        #     theta=-45 * DEGREES, phi=60*DEGREES)

        matrix = Matrix([[1, 2]])
        self.add(matrix)
        self.wait(5)


class RubiksCube(VGroup):
    CONFIG = {
        "colors": [
            "#FFD500",  # Yellow
            "#C41E3A",  # Orange
            "#009E60",  # Green
            "#FF5800",  # Red
            "#0051BA",  # Blue
            "#FFFFFF"   # White
        ],
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        vectors = [OUT, RIGHT, UP, LEFT, DOWN, IN]
        faces = [
            self.create_face(color, vector)
            for color, vector in zip(self.colors, vectors)
        ]
        VGroup.__init__(self, *it.chain(*faces), **kwargs)
        self.set_shade_in_3d(True)

    def create_face(self, color, vector):
        squares = VGroup(*[
            self.create_square(color)
            for x in range(9)
        ])
        squares.arrange_in_grid(
            3, 3,
            buff=0
        )
        squares.set_width(2)
        squares.move_to(OUT, OUT)
        squares.apply_matrix(z_to_vector(vector))
        return squares

    def create_square(self, color):
        square = Square(
            stroke_width=3,
            stroke_color=BLACK,
            fill_color=color,
            fill_opacity=1,
            side_length=1,
        )
        square.flip()
        return square
        # back = square.copy()
        # back.set_fill(BLACK, 0.85)
        # back.set_stroke(width=0)
        # back.shift(0.5 * IN)
        # return VGroup(square, back)

    def get_face(self, vect):
        self.sort(lambda p: np.dot(p, vect))
        return self[-(12 + 9):]


class RubuiksCubeOperations(SpecialThreeDScene):
    def construct(self):
        self.set_camera_orientation(**self.get_default_camera_position())
        self.begin_ambient_camera_rotation()
        cube = RubiksCube()
        # cube.shift(2.5 * RIGHT)

        self.add(cube)
        # self.play(
        #     Rotate(cube.get_face(RIGHT), 90 * DEGREES, RIGHT),
        #     run_time=2
        # )
        # self.play(
        #     Rotate(cube.get_face(DOWN), 90 * DEGREES, UP),
        #     run_time=2
        # )
        # self.wait()
        # self.play(
        #     cube.shift, 5 * LEFT,
        #     FadeIn(cube2)
        # )
        # self.play(
        #     Rotate(cube2.get_face(DOWN), 90 * DEGREES, UP),
        #     run_time=2
        # )
        # self.play(
        #     Rotate(cube2.get_face(RIGHT), 90 * DEGREES, RIGHT),
        #     run_time=2
        # )
        self.wait(6)
