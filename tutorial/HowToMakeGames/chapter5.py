from manimlib.imports import *
from gametutorialslib.imports import *

import os
import pyclbr


class CameraFollowVectorDistance(DefaultThreeDScene):
    def construct(self):
        cam_svg = CameraSVG(height=1.5)
        cam_svg.to_edge(LEFT+UP)
        cam_svg.shift(DOWN)

        cube = Cube(fill_color="#e00b0b", side_length=1)
        cube.center()
        self.mobject_face_default_perspective(cube)

        vec_cam_dist = Arrow(start=cube.get_center(),
                             end=cam_svg.get_center() + [0.6, 0, 0], color=YELLOW)

        vec_brace = Brace(
            vec_cam_dist, direction=UP+RIGHT*0.35)
        vec_brace_text = vec_brace.get_tex(
            "distanciaProJogador").rotate(-19*DEGREES)

        text_1 = ProgrammingTextMObject(
            "this.transform.position = playerController.transform.position")
        text_1.scale(0.7)
        text_1.to_edge(LEFT+DOWN)
        text_1.shift(UP*1.5)

        text_2 = ProgrammingTextMObject(
            "+ distanciaProJogador", fill_color=YELLOW)
        text_2.scale(0.7)
        text_2.next_to(text_1)

        # animations
        cam_svg.center()
        cam_svg.to_edge(LEFT)
        self.play(GrowFromCenter(cam_svg), GrowFromCenter(cube))
        self.wait(2)

        self.play(ApplyMethod(cam_svg.move_to, cube),
                  ShowCreation(text_1))
        self.wait(2)

        cam_copy = cam_svg.copy()
        cam_copy.center()
        cam_copy.to_edge(LEFT+UP)
        cam_copy.shift(DOWN)
        self.play(ShowCreation(vec_cam_dist, run_time=1.4), FadeIn(vec_brace, run_time=1.4), FadeIn(vec_brace_text, run_time=1.4), ApplyMethod(
            cam_svg.move_to, cam_copy), ShowCreation(text_2))

        self.wait(5)
