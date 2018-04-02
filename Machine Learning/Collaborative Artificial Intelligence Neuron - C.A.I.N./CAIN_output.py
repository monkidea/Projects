"""CAIN Output Unit
Collaborative Artificial Intelligence Neuron v1.0"""

import os


class CAIN_OUTPUT:
    """Output using classes for ease of usage."""

    def __init__(self, output_content, speech_output=True):
        """Simple initialisation"""
        self.output_content = output_content
        self.speech_output = speech_output
        # Output mode is set to True for voice and False for text.

    def responder(self):
        """Responder function invokes a response from the system
           using the requested output mode"""
        if(self.speech_output):  # If output mode is set to voice
            os.system("say '{}'".format(str(self.output_content)))
        else:
            print(str(self.output_content))  # Standard vanilla output
