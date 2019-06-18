#!/bin/bash
set -e

glaze --input data/Georgia.json
NUMPNGS1=$(find data/ -type f -name "*.png" | wc -l)
if [ $NUMPNGS1 != 69 ]
then
    echo "Test failed on first command."
    exit 1
else
    echo "Success on first command!"
fi
echo

glaze --input data/ --output data/img/
NUMPNGS2=$(find data/img/ -type f -name "*.png" | wc -l)
if [ $NUMPNGS2 != 69 ]
then
    echo "Test failed on second command."
    exit 1
else
    echo "Success on second command!"
fi
echo
