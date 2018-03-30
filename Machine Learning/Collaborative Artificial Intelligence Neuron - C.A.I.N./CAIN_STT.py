"""CAIN Speech-To-Text Unit
Collaborative Artificial Intelligence Neuron v1.0"""

import speech_recognition as sr


class CAIN_STT:
    """Creating Classes for ease of use and implementation."""

    def __init__(self, speech_input):
        """Simple Initialisation function"""
        self.speech_input = speech_input
        CAIN_STT.process_speech(self.speech_input)

    def process_speech(speech_to_process):
        recog = sr.Recognizer()
        try:
            response = recog.recognize_google(speech_to_process)
            return response
        except sr.UnknownValueError:
            print("[!] SpeechRecognition could not understand audio!")
        except Exception as e:
            print("[!] Exception Occured! Details are :")
            print(e)
