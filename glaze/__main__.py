#!/bin/python

from absl import flags, app

FLAGS = flags.FLAGS

FILE_FORMATS = ["png", "jpg", "pdf"]

flags.DEFINE_string("input", None, "Input.")
flags.mark_flag_as_required("input")
flags.DEFINE_string("output", None, "Output.")
flags.DEFINE_boolean(
    "from-json", False, "If True, --input must be the path to a .json file."
)
flags.DEFINE_enum("format", "png", FILE_FORMATS, "Format.")


def visualize(argv):
    pass


def main():
    app.run(visualize)
