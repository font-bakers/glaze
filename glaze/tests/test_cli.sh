#!/bin/bash
set -e

glaze --input data/
glaze --input data/Georgia.json
glaze --input data/ --output data/img/
