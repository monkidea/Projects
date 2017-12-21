#!/usr/bin/env python3

"""Program to do some data analysis."""

import optparse
import sys

"""Command line args"""

parser = optparse.OptionParser()
parser.add_option("-s", dest="search_term", help="The term to analyse")
parser.add_option("--search-all", dest="searchallbool", help="Use to analyse all terms")
parser.add_option("-f", dest="inpfile", help="Input file")

(options, arg) = parser.parse_args()

inp_file = options.inpfile
search_t = options.search_term
all_s_bool = options.searchallbool

if search_t is None and all_s_bool is None or inp_file is None:
    parser.print_help()
    sys.exit()

elif all_s_bool is None:
    all_s_bool = False

try:
    data_file = open(str(inp_file), "r")
except IOError:
    print("Could not open data_file")
    sys.exit()

data_list = list()
for line in data_file.readlines():
    data_list.append(line)

if(all_s_bool is False):
    counter = 0
    occured_instances = list()
    for i in range(len(data_list)):
        if search_t in data_list[i]:
            counter += 1
            occured_instances.append(data_list[i])
    print("The search term occured {} times".format(counter))
    percentage = (counter / len(data_list)) * 100
    print("Element '{}' covers {}% of the data space.".format(search_t, int(percentage)))
    print("The instances in which the search term occured are :\n")
    for i in occured_instances:
        print(i)
    sys.exit()

else:
    new_data_list = list()
    already_occured = list()
    for i in range(len(data_list)):
        # Splitting elements using '&' delimiter
        if "&" in data_list[i]:
            tempvar = data_list[i].split(' & ')
            for elem in tempvar:
                new_data_list.append(elem)
        else:
            new_data_list.append(data_list[i])
    
    # Now checking occurence and calculating percentage
    for elem in new_data_list:
        if elem.rstrip('\n') not in already_occured:
            elem = elem.rstrip('\n')
            counter = 0
            occured_instances = list()
            for i in range(len(new_data_list)):
                if elem in new_data_list[i]:
                    counter += 1
                    occured_instances.append(new_data_list[i])
            print("The search term {} occured {} times".format(elem, counter))
            percentage = (counter / len(new_data_list)) * 100
            print("Element '{}' covers {}% of the data space.".format(elem,percentage))
            print("The instances in which the search term occured are :\n")
            for i in occured_instances:
                print(i+"\n")
            already_occured.append(elem)
        else:
            pass
