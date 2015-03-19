#!/usr/bin/python
# Swathi Amarala
# main_running_median.py - Running median for the number
# of words per line of text.

import sys, os, re
import numpy as np

def main(argv):
    rootDir = str(argv[0])
    countList = [] # accumulative list of number of words per line
    runMedList = [] # accumulative list of running median

    # parse directory
    for dirName, subDirList, fileList in os.walk(rootDir):
        for file in sorted(fileList):
            if file.startswith('.'):
                continue # ignore OS X hidden files
            fp = open(dirName+'/'+file, 'r')
            # read file content line by line
            for line in fp:
                line = line.lower()
                # merge words separated by hyphen
                line = line.replace('-','')
                # split line into words on encountering
                # non-alphanumeric characters \W+
                wordList = filter(lambda elm: elm != '', re.split('\W+', line))
                countList.append(len(wordList))
                # compute medium using numpy
                runMedList.append(np.median(np.array(countList)))
            fp.close()

    # print to a file
    fp = open(str(argv[1]), 'w')
    for elm in runMedList:
        fp.write(str(elm)+'\n')
    fp.close()
    print 'Running median: output successfully written!'

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print 'Error...'
        print 'usage: python ./src/main_running_median.py ./wc_input ./wc_output/med_result.txt'
        sys.exit()
    
    main(sys.argv[1:])