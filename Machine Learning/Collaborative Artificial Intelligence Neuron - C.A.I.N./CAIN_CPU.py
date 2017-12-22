"""CAIN Command Processing Unit
Collaborative Artificial Intelligence Neuron v1.0"""

import os


class CAIN_CPU:
    """Command Processing using classes because it's convenient"""

    def __init__(self, command):
        """Initiating the values"""
        self.command = command

    def execute_command(self):
        """Main command execution function"""
        # Dumping a list of files in CAIN path
        os.system("ls /Users/shourojitdutt/CAIN/CAIN_exec > /Users/shourojitdutt/CAIN/checkfile.txt")
        check_file = open("/Users/shourojitdutt/CAIN/checkfile.txt", "r")
        # Reading file information into temporary buffer
        read_check_file = check_file.readlines()
        for i in len(read_check_file):
            if self.command in read_check_file[i]:  # If found in CAIN path
                buff = read_check_file[i]   # Dumping into another buffer
                os.system("python3.6 "+buff[:-1])   # Executing the file from CAIN path
            else:
                os.system(self.command)     # Did not find file in CAIN path
        check_file.close()  # Closing file to avoid buffer flushing issues
        # Removing checkfile since it isn't needed anymore
        os.system("rm -f /Users/shourojitdutt/CAIN/checkfile.txt")
