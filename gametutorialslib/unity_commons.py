from gametutorialslib.threed_commons import *

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
