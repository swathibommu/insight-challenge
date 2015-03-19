# insight-challenge
Python implementation of word count and running median problems. 

The source files - main_word_count.py and main_running_median.py can be found in src. 

Use run.sh to run these two programs.

main_running_median.py uses numpy and this dependency is automatically installed by run.sh using apt-get.

The input text files are in wc_input directory, which is of 3.9MB size. This directory contains 772 news articles from different news websites such as cbc.ca, cbsnews, cnet, globeandmail, etc. The html files were parsed to extract the body text.

Words with hyphens are concatenated so that well-known is counted as wellknown. 
I keep all alphanumeric characters and punctuation marks removed. 

Output of main_word_count.py is written to wc_result.txt.
Output of main_running_median.py is written to med_result.txt.
