"""CAIN Command Processing Unit
Collaborative Artificial Intelligence Neuron v1.0"""

import os
import sys


class CAIN_CPU:
    """Command Processing using classes because it's convenient"""

    def __init__(self, command):
        """Initiating the values"""
        self.command = command
        # CAIN_PATHS is a variable that can be adjusted if one wants
        # to add or remove paths to check in.
        self.CAIN_PATHS = ["/Users/shourojitdutt/CAIN/CAIN_exec"]
        self.output_context = ""

    def execute_command(command, CAIN_PATHS):
        """Main command execution function"""
        # Dumping a list of files in CAIN path
        for path in range(len(CAIN_PATHS)):
            os.system("ls " + str(CAIN_PATHS[path]) + " >> "
                      + "/Users/shourojitdutt/CAIN/checkf.txt")
        check_file = open(
            "/Users/shourojitdutt/CAIN/checkf.txt", "r")
        # Reading file information into temporary buffer
        read_check_file = check_file.readlines()
        check_file.close()  # Closing file to avoid buffer flushing issues
        # Removing checkfile since it isn't needed anymore
        os.system("rm -f /Users/shourojitdutt/CAIN/checkf.txt")
        for i in range(len(read_check_file)):
            # If found in CAIN path
            if command in read_check_file[i]:
                buff = read_check_file[i]   # Dumping into another buffer
                # Execute file from CAINpath
                CAIN_CPU.self.output_context = "Command '{}' ".format(command)
                CAIN_CPU.self.output_context += "found in CAIN Path, executing"
                for path in CAIN_PATHS:
                    try:
                        os.system("python3.6 " + path + "/" +
                                  str(buff).rstrip())
                    except Exception as e:
                        print("Exception Occured :\n{}".format(e))
                        sys.exit(1)
        # If it reached here, it did not find file in CAIN path.

        CAIN_CPU.self.output_context = "Command '{}' ".format(command)
        CAIN_CPU.self.output_context += "not found in CAIN Path, system"
        CAIN_CPU.self.output_context += " executing"
        os.system(command)
