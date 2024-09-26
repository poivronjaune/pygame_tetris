from config import *

class Colors:
    COLOR_0 = (44, 44, 127)
    COLOR_1 = (26, 31, 40)
    COLOR_2 = (47, 230, 23)
    COLOR_3 = (232, 18, 18)
    COLOR_4 = (226, 116, 17)
    COLOR_5 = (237, 234, 4)
    COLOR_6 = (166, 0, 247)
    COLOR_7 = (21, 204, 209)
    COLOR_8 = (13, 64, 216)

    @classmethod
    def get_cell_colors(cls):
        return [cls.COLOR_1, cls.COLOR_2, cls.COLOR_3, cls.COLOR_4, cls.COLOR_5, cls.COLOR_6, cls.COLOR_7, cls.COLOR_8]