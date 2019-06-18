#!/bin/python

from glob import glob
import os
import logging
from absl import flags, app
import matplotlib.pyplot as plt
from tqdm import tqdm
from .render import render
from .utils import read_json, get_output_filename

FLAGS = flags.FLAGS

LOG_LEVELS = ["debug", "info", "warning", "error", "critical"]

flags.DEFINE_string("input", None, "Path to input file. Must be a .json file.")
flags.mark_flag_as_required("input")
flags.DEFINE_string("output", None, "Output.")
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

    if os.path.isdir(FLAGS.input):
        glyphs = []
        for json_file in glob(os.path.join(FLAGS.input, "*.json")):
            glyphs.extend(read_json(json_file))
        font_path = FLAGS.input
    elif os.path.isfile(FLAGS.input):
        glyphs = read_json(FLAGS.input)
        font_path, _ = os.path.split(FLAGS.input)
    else:
        msg = (
            "--input not understood. Expected .json file or directory of "
            ".json files, got {}".format(FLAGS.input)
        )
        raise ValueError(msg)

    if FLAGS.output and not os.path.exists(FLAGS.output):
        os.mkdir(FLAGS.output)

    num_renders = 0
    num_exceptions = 0
    for font_name, glyph_name, glyph in tqdm(glyphs):
        try:
            output_filename = get_output_filename(font_path, font_name, glyph_name)
            render(glyph)
            plt.savefig(output_filename)
            num_renders += 1
        except Exception:
            logger.exception("Failed to render {} {}.".format(font_name, glyph_name))
            num_exceptions += 1
        finally:
            plt.close("all")

    msg = "Successfully rendered {} ({:.2f}%) glyph(s). See log file for details.\n".format(
        num_renders, 100 * num_renders / (num_renders + num_exceptions)
    )
    print(msg)


def main():
    """ Main entry point of `glaze`. """
    app.run(visualize)
