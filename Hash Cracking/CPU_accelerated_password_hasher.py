#!/usr/bin/env python3
import sys
import hashlib
import optparse
import multiprocessing


"""Main hashing function"""


def hash_vector(password, hashtype, f_to_write):
    hsh = hashlib.new(hashtype)
    hsh.update(password.encode("utf-8"))  # Avoiding errors.
    print("[∞] Current hash is :", str(hsh.hexdigest()))
    f_to_write.write(str(hsh.hexdigest()))
    f_to_write.write("\n")  # Avoiding flushing issues
    f_to_write.close()  # Need to close file here else it won't write.


"""Parsing Options:
    1) Output File
    2) Hash Type
    3) Password List"""

parser = optparse.OptionParser()
parser.add_option("--output-file", dest="op_file", help="The output file of hashes")
parser.add_option("--hash-type", dest="type_h", help="Type of hash")
parser.add_option("--pass-list", dest="pw_list", help="List of passwords")

(options, arg) = parser.parse_args()

if options.type_h is None or options.pw_list is None:
    parser.print_help()
    sys.exit()

htype = options.type_h
opfile = options.op_file
pwlist = options.pw_list

if __name__ == '__main__':
    try:
        opf = open(str(opfile), "w", encoding="utf-8")
    except IOError:
        print("[!] Cannot open outputfile")
        sys.exit()
    if pwlist is not None:
        try:
            pwl = open(str(pwlist), "r", encoding="utf-8")
        except IOError:
            print("[!] Cannot open password list")
            sys.exit()
        for line in pwl.readlines():
            """Using the multiprocessing library here
               to use CPU based acceleration to speed up things.
               It may be worth making a copy of this with
               CUDA Acceleration for when I'm deploying to the cloud."""
            multi_p = multiprocessing.Process(target=hash_vector,
                                              args=(line, htype, opf))
            multi_p.start()
        pwl.close()
        opf.close()
        sys.exit()
    else:
        opf.close()
        pwl.close()
        print("[!] Password list is empty!")
        sys.exit()
