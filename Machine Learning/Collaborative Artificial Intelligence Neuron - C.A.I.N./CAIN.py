"""Collaborative Artificial Intelligence Neuron v1.0"""

import sys
from CAIN_FrontEnd import CAIN_FrontEnd as CFE
from CAIN_STT import CAIN_STT as CSTT
from CAIN_SPU import CAIN_SPU as CSPU
from CAIN_CPU import CAIN_CPU as CCPU
from CAIN_output import CAIN_output as COP


def CAIN_Shell():
    """Simple function to run the shell, take input and send it through
       CAIN's libraries.
       Going to be using the CAIN_FrontEnd library here to take input."""
    front_end_outputs = CFE()
    front_end_outputs.isspeech = CFE.take_input()
    if front_end_outputs.isspeech:  # If we have spoken input
        # Sending speech input to CAIN's libraries
        Run_CAIN(front_end_outputs.AUDIO_INPUT, True)
    else:  # We have text input
        # Sending text input to CAIN's libraries
        Run_CAIN(front_end_outputs.TYPED_INPUT, False)


def Run_CAIN(shell_input, is_audio):
    """Function that'll run the input through the rest of CAIN's libraries."""
    if is_audio:  # If shell_input is in the form of audio
        stt_var = CSTT(shell_input)  # Speech to Text Conversion
        stt_var.text_output = CSTT.process_speech(stt_var.speech_input)
        spu_var = CSPU(stt_var.text_output)  # Semantics Processing
        spu_output = spu_var.Separation_Engine(spu_var.stt_output)
        for output in spu_output:
            temp_cpu_var = CCPU(output)  # Command Execution
            CCPU.execute_command(temp_cpu_var.command, temp_cpu_var.CAIN_PATHS)
            # Here, we give speech output as True since audio was provided.
            cop_var = COP(temp_cpu_var.output_context, True)
            cop_var.responder()  # Output returning

    else:  # If shell_input is in the form of text
        if shell_input == "exit":
            print("(( CAIN <Exiting> ))")
            sys.exit(0)
        spu_var = CSPU(shell_input)  # Semantics Processing
        spu_output = spu_var.Separation_Engine(spu_var.stt_output)
        for output in spu_output:
            temp_cpu_var = CCPU(output)  # Command Execution
            CCPU.execute_command(temp_cpu_var.command, temp_cpu_var.CAIN_PATHS)
            # Here, we give speech output as False since Text was provided.
            cop_var = COP(temp_cpu_var.output_context, False)
            cop_var.responder()  # Output returning


while True:
    CAIN_Shell()
