#!/usr/bin/env python3

"""The earlier non-optimized version
   took 21 minutes and 4 seconds,
   a single process version of this
   took 16 mins 14 seconds,
   while this optimized version took
   9 minutes and 14 seconds on the same
   list of sha512 hashes."""

import hashlib
import sys
import optparse
import multiprocessing

"""Main dictionary attack function.
   Taking the dictionary as input this time.
   Earlier iteration involved taking the
   dictionary file and then opening it within the function
   and adding the contents to a dictionary variable.
   This had a time complexity of order of O(n^2);
   Now however by doing this addition in the main
   function, the time complexity is reduced to the order of O(n)."""

def dict_attack_vector(pwhash, hashtype, dictionary):
    bool_vector = False
    for dict_val in dictionary:
        hashval = hashlib.new(hashtype)
        # Encoding now in UTF-8 to avoid flushing issues.
        hashval.update(dict_val.encode("utf-8"))
        if hashval.hexdigest() == pwhash:
            print("[∞] Found!")
            print("[∞] Hash is", hashval.hexdigest())
            print("[∞] Password is :", dict_val)
            bool_vector = True
            break  # Breaking if found so that iterations don't continue
        else:
            pass  # Avoiding any loop issues
    if bool_vector is False:  # If it reaches this point, pw is not found
        print("[!] Password not found in given dictionary!")


"""Parsing Options :
    1) Hash List
    2) Hash Type
    3) Dictionary"""


parser = optparse.OptionParser()
parser.add_option("--hash-list", dest="hash_l", help="List of hashes")
parser.add_option("--hash-type", dest="htype", help="Type of hash")
parser.add_option("--dictionary", dest="opt_dict", help="The dictionary")

(options, arg) = parser.parse_args()

if options.htype is None or options.opt_dict is None:
    parser.print_help()
    sys.exit()

type_h = options.htype
dictlist = options.opt_dict
h_list = options.hash_l

if __name__ == '__main__':
    if h_list is not None:
        try:
            to_crack = [line.strip() for line in open(h_list)]
        except IOError:
            print("[!] IO Error! Can't open hash list!")
            sys.exit()
        net_dict = list()  # Creating list here to reduce time complexity
        try:
            df = open(str(dictlist), "r")  # Dictionary file
            for dval in df.readlines():  # Parsing through df
                dval.strip()  # Getting rid of the '\n' at the end
                net_dict.append(dval)
            df.close()  # Closing df to avoid flushing issues
        except IOError:
            print("[!] IO Error! Can't open dictionary file!")
            sys.exit()
        for hashes in to_crack:
            """ Using the Multiprocessing library to speed it up.
                May be worth it to create a copy of this with
                CUDA Acceleration for when you're deploying
                this code to the cloud through AWS in order
                to maximize power."""
            multi_p = multiprocessing.Process(target=dict_attack_vector,
                                              args=(hashes, type_h, net_dict))
            multi_p.start()
        sys.exit()
    else:
        print("[!] Hash list is empty!")
        sys.exit()
