import json
import os
from absl import flags
import numpy as np

FLAGS = flags.FLAGS

UPPERCASES = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWERCASES = {character.lower() for character in UPPERCASES}
NUMERALS = {
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
}
SPECIALS = {
    "exclam",
    "numbersign",
    "dollar",
    "percent",
    "ampersand",
    "asterisk",
    "question",
    "at",
}
CHARACTER_SET = UPPERCASES.union(LOWERCASES, NUMERALS, SPECIALS)


def read_json(filename):
    """
    Read a serialized .json file (such as those produced by `knead`).

    Parameters
    ----------
    filename : string
        Path to a .json file.

    Returns
    -------
    A dictionary of lists of np.ndarrays. Each item in the dictionary is one
    glyph: a list of contours, where each contour is an np.ndarray with shape
    (num_curves, 3, 2).
    """
    with open(filename, "r") as f:
        json_dict = json.load(f)

    font_np = {}
    for glyph_name, glyph in json_dict.items():
        contours_np = []
        for contour in glyph:
            contours_np.append(np.asarray(contour))
        font_np[glyph_name] = contours_np

    return font_np


def get_output_filename(font_path, glyph_name):
    """
    Parameters
    ----------
    font_path, glyph_name : strings
        Names of font and glyph, respectively.
        E.g. "data/Georgia" and "A", respectively.

    Returns
    -------
    output_filename : string
    """
    # Some file systems are case-insensitive
    if glyph_name in UPPERCASES:
        glyph_name += "_upper"
    elif glyph_name in LOWERCASES:
        glyph_name += "_lower"

    output_filename = font_path + "." + glyph_name + "." + FLAGS.format
    if FLAGS.output:
        _, filename = os.path.split(output_filename)
        output_filename = os.path.join(FLAGS.output, filename)

    return output_filename
