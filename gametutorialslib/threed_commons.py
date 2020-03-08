from manimlib.constants import *
from manimlib.mobject.svg.tex_mobject import *
from manimlib.mobject.svg.svg_mobject import *
from manimlib.scene.three_d_scene import *


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


class SVGMObjectBase(SVGMobject):
    def __init__(self, file_name=None, **kwargs):
        digest_config(self, kwargs)
        self.file_name = file_name or self.file_name
        abs_path = os.path.dirname(os.path.abspath(__file__))
        SVGMobject.__init__(self, abs_path + "/" + self.file_name, **kwargs)


class CameraSVG(SVGMObjectBase):
    CONFIG = {
        "file_name": "res/camera_1024",
        "fill_opacity": 1.0,
        "should_center": True
    }
