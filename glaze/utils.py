import json
import numpy as np


def read_json(json_filename):
    """
    Read a serialized .json file, returning a dict of np.ndarrays.
    """
    with open(json_filename, "r") as f:
        json_dict = json.load(f)

    font_np = {}
    for glyph_name, glyph in json_dict.items():
        contours_np = []
        for contour in glyph:
            contours_np.append(np.asarray(contour))
        font_np[glyph_name] = contours_np

    return font_np
