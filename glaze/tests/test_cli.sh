#!/bin/bash
set -e

glaze --directory data/
NUMPNGS1=$(find data/ -type f -name "*.png" | wc -l)
if [ $NUMPNGS1 != 69 ]
then
    echo "Test failed on first command."
    exit 1
else
    echo "Success on first command!"
fi
echo

glaze --files data/json/* --output data/renders/ --grid
NUMPNGS2=$(find data/renders/ -type f -name "*.png" | wc -l)
if [ $NUMPNGS2 != 69 ]
then
    echo "Test failed on second command."
    exit 1
else
    echo "Success on second command!"
fi
echo
