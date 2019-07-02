#!/bin/python

from glob import glob
from datetime import datetime
import os
import logging
from absl import flags, app
import matplotlib.pyplot as plt
from tqdm import tqdm
from .render import render
from .utils import read_json, get_output_filename

FLAGS = flags.FLAGS

LOG_LEVELS = ["debug", "info", "warning", "error", "critical"]

flags.DEFINE_string("directory", None, "Directory.")
flags.DEFINE_list("files", None, "Files.")
flags.DEFINE_string(
    "output", None, "Path to output. Defaults to present working directory."
)
flags.DEFINE_integer(
    "num_points", 32, "Number of points per Bezier curve. Defaults to 32."
)
flags.DEFINE_list(
    "lim", [-0.3, 1.2], "x and y limits for rendered glyphs. Defaults to [-0.3, 1.2]"
)
flags.DEFINE_boolean(
    "grid", False, "If True, plots axes and gridlines. Defaults to False."
)
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

    if bool(FLAGS.directory) == bool(FLAGS.files):
        msg = "Exactly one of `--directory` and `--files` must be specified."
        raise ValueError(msg)

    if FLAGS.directory:
        glyphs = []
        for filename in glob(os.path.join(FLAGS.directory, "json/*")):
            glyphs.extend(read_json(filename))
        time = datetime.now().strftime("%H%M-%d-%m")
        output_dir = os.path.join(FLAGS.directory, "renders-{}".format(time))
    elif FLAGS.files:
        glyphs = []
        for regex in FLAGS.files:
            for filename in glob(regex):
                glyphs.extend(read_json(filename))
        output_dir = FLAGS.output if FLAGS.output else os.getcwd()

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    FLAGS.lim = [float(i) for i in FLAGS.lim]

    num_renders = 0
    num_exceptions = 0
    for font_name, glyph_name, glyph in tqdm(glyphs):
        try:
            output_filename = get_output_filename(output_dir, font_name, glyph_name)
            render(glyph, num_points=FLAGS.num_points, lim=FLAGS.lim, grid=FLAGS.grid)
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
