#!/usr/bin/python
# Swathi Amarala
# main_word_count.py - parses a given directory of text files and
# outputs the number of occurrences for each word.

import sys, os, re
from collections import Counter
from operator import itemgetter

def main(argv):
    rootDir = str(argv[0])
    wordList = [] # accumulative list for all words in all text files

    # parse directory
    for dirName, subDirList, fileList in os.walk(rootDir):
        for file in fileList:
            if file.startswith('.'):
                continue # ignore OS X hidden files
            fp = open(dirName+'/'+file, 'r')
            # read file content line by line
            for line in fp:
                line = line.lower()
                line = line.replace('-','') # Take care of hyphens
                # split line into words on encountering
                # non-alphanumeric characters \W+
                [wordList.append(elmList) for elmList in \
                 filter(lambda elm: elm != '', re.split('\W+', line))]
            fp.close()
    # count occurrences of each word in the wordList
    counts = Counter(wordList)
    # sort by key value in ascending order
    c = sorted(counts.items(), key = itemgetter(0))

    # output to a file
    fp = open(str(argv[1]), 'w')
    for elm in c:
        data = [elm[0], str(elm[1])]
        fp.write('{0[0]:<20}{0[1]}'.format(elm)+'\n')
    fp.close()
    print 'Word count: output successfully written!'

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print 'Error...'
        print 'usage: python ./src/main_word_count.py ./wc_input ./wc_output/wc_result.txt'
        sys.exit()
    
    main(sys.argv[1:])