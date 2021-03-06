"""CAIN FrontEnd Unit
Collaborative Artificial Intelligence Neuron v1.0"""

import speech_recognition as sr
from pynput import keyboard as kb


class CAIN_FrontEnd:
    """Implementing through classes as always because it
       works better."""

    def __init__(self):
        self.TYPED_INPUT = ""
        self.AUDIO_INPUT = None
        self.isspeech = None

    def take_input():
        """Starting this 'pynput' keyboard listener may be subject to some
           restrictions on your platform.

           On Mac OSX, one of the following must be true:

                [∞] The process must run as root.
                [∞] Your application must be white listed under Enable access
                    for assistive devices. Note that this might require that
                    you package your application, since otherwise the entire
                    Python installation must be white listed.

           On Windows, virtual events sent by other processes may not be
           received. This library takes precautions, however, to dispatch any
           virtual events generated to all currently running listeners of the
           current process.
           """
        print("<<    Taking Input    >>")
        recog = sr.Recognizer()  # Simple Recognizer initialization.
        # Now setting placeholder values for Microphone, adjust as required.
        with sr.Microphone(device_index=0, sample_rate=48000,
                           chunk_size=2048) as source:
            with kb.Listener(on_press=CAIN_FrontEnd.on_press) as listener:
                listener.start()  # Starting the keyboard listener.
                while listener is None:  # While user has not typed anything.
                    print("(( CAIN <Spoken> ))")  # Taking spoken input.
                    CAIN_FrontEnd.self.AUDIO_INPUT = recog.listen(source)
                    return True  # Indicates audio output.
                # If it gets here, it means that user started typing.
                listener.join()
                return False  # Indicates text output.

    def on_press(key):
        print("(( CAIN <Typed> ))")
        while key != kb.Key.enter:
            CAIN_FrontEnd.self.TYPED_INPUT += key
        return CAIN_FrontEnd.self.TYPED_INPUT
