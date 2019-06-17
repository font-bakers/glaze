#!/bin/python

import os
import logging
from absl import flags, app
import matplotlib.pyplot as plt
from tqdm import tqdm
from .render import render
from .utils import read_json, get_output_filename

FLAGS = flags.FLAGS

FILE_FORMATS = ["png", "jpg", "pdf"]
LOG_LEVELS = ["debug", "info", "warning", "error", "critical"]

flags.DEFINE_string("input", None, "Path to input file. Must be a .json file.")
flags.mark_flag_as_required("input")
flags.DEFINE_string("output", None, "Output.")
flags.DEFINE_enum("format", "png", FILE_FORMATS, "Format.")
flags.DEFINE_enum(
    "loglevel", "critical", LOG_LEVELS, "Logging level. Defaults to `logging.CRITICAL`."
)


def setup_logging():
    logger = logging.getLogger("glaze")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    file_handler = logging.FileHandler("glaze.log")
    file_handler.setLevel(logging.DEBUG)  # Lowest logging level.

    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, FLAGS.loglevel.upper(), None))

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def visualize(argv):
    logger = setup_logging()
    font_dict = read_json(FLAGS.input)
    font_path, _ = os.path.splitext(FLAGS.input)

    if FLAGS.output and not os.path.exists(FLAGS.output):
        os.mkdir(FLAGS.output)

    num_visualizations = 0
    num_exceptions = 0
    for glyph_name, glyph in tqdm(font_dict.items()):
        try:
            output_filename = get_output_filename(font_path, glyph_name)
            fig = render(glyph)
            plt.savefig(output_filename)
            plt.close(fig)
            num_visualizations += 1
        except Exception:
            logger.exception("Failed to visualize {} {}".format(font_path, glyph_name))
            num_exceptions += 1


def main():
    """ Main entry point of `glaze`. """
    app.run(visualize)
