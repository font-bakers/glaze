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
    A lists of 3-tuples. Each tuple consists of the font name (a string), the
    glyph name (a string), and a list of np.ndarrays, each representing one
    contour and having shape (num_curves, 3, 2).
    """
    _, font_file = os.path.split(filename)
    font_name, _ = os.path.splitext(font_file)

    with open(filename, "r") as f:
        json_dict = json.load(f)

    glyphs = []
    for glyph_name, glyph in json_dict.items():
        contours_np = []
        for contour in glyph:
            contours_np.append(np.asarray(contour))
        glyphs.append((font_name, glyph_name, contours_np))

    return glyphs


def get_output_filename(output_dir, font_name, glyph_name):
    """
    Parameters
    ----------
    output_dir, glyph_name : strings
        Output directory and names of font and glyph, respectively.
        E.g. "data/", "Georgia" and "A", respectively.

    Returns
    -------
    output_filename : string
    """
    # Some file systems are case-insensitive
    if glyph_name in UPPERCASES:
        glyph_name += "_upper"
    elif glyph_name in LOWERCASES:
        glyph_name += "_lower"

    output_filename = os.path.join(output_dir, font_name + "." + glyph_name + ".png")
    if FLAGS.output:
        _, filename = os.path.split(output_filename)
        output_filename = os.path.join(FLAGS.output, filename)

    return output_filename
