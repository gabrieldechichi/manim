from manimlib.constants import *
from manimlib.mobject.svg.tex_mobject import *
from manimlib.mobject.svg.svg_mobject import *


class ProgrammingTextMObject(TextMobject):
    CONFIG = {
        "fill_color": "#BDB76B",
        "arg_separator": "",
        "tex_to_color_map": {"this": "#387df2", "=": WHITE, ".": WHITE, "+": WHITE}
    }

    def generate_single_string_mobject(self, tex_strings):
        parent_result = super().generate_single_string_mobject(tex_strings)
        return parent_result.replace("=", " = ").replace("+", " + ")
