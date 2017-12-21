Introduction :
--------------
This is a program that I had initially made to figure out what I should study for my Nanotechnology Exam.
It was a closed book examination and I had a soft copy of 6 of the previous years' question papers, so I made a file containing
the topics of each question of each question paper and made this program in order to figure out what I should study.

This program will take a file as input and tell you the number of occurences and percentage of occurence of either the
provided search term, or each search term that occurs in the file. Search terms are seperated both by next-line ["\n"]
characters and by "&" characters. If you would like to change the delimiter from "&" to something else, then change line 58
of the program.

Usage :
-------
Just to clarify, you can check the usage options by typing in "./file_data_analyser.py" and hitting Enter/Return on your
terminal.

    (i) To search for a specific data item in file :
    
    ./file_data_analyser -s [SEARCH TERM] -f [PATH TO INPUT FILE]
    
    (ii) To search for all possible data items in file :
    
    ./file_data_analyser --search-all True -f [PATH TO INPUT FILE]
