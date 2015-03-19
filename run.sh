#!/usr/bin/env bash

# Load all dependencies
apt-get install python-numpy

# Set proper permissions to programs
chmod a+x ./src/main_word_count.py
chmod a+x ./src/main_running_median.py

# Execute programs
python ./src/main_word_count.py ./wc_input ./wc_output/wc_result.txt
python ./src/main_running_median.py ./wc_input ./wc_output/med_result.txt