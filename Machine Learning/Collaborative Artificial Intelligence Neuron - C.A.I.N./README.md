Introduction :
--------------
This is a barebones A.I. skeleton for a personal-assistant style A.I. (like the Google Assistant or Siri) that is meant to
help in accelerating the development process of projects in the same genre.

Language :
----------
Python 3.6

Structural Model :
------------------

                                [ Front End Speech / Text Input ]
                                              |
                                              |
                                              |
                                              
                          [ Check for Speech Synthesis Requirement ]
                                  |                     |
                              Yes |                     | No
                                  |                     |
                                                        |
                    [ Speech-to-Text Conversion ]       |  
                                  |                     |
                                  |                     |
                                  |                     |
                                  
                          [ Semantics Processing Unit (SPU) ]
                                          |
                                          | Instruction in the form of Command Syntax
                                          |
                                          
                            [ Command Processing Unit (CPU) ]
                                          |
                                          | Result
                                          |
                                          
                                [ Output to Terminal ]
                                

Operating Systems Supported :
-----------------------------
MacOS, Linux & other UNIX or *NIX based systems. Please note that the sound output in the output library only works for
MacOS. Please change line 20 of the output library in order to get it working on Linux.

Work Done :
-----------
[∞] CPU

[∞] Output Library

Work TODO :
-----------
[Ω] Finish writing the detailed descriptions for the operation and working of each sub-unit of C.A.I.N.

[Ω] Input Unit

[Ω] Speech Requirement Checking Unit

[Ω] Speech-to-Text Unit

[Ω] SPU

Trivia :
--------
I decided to call this CAIN as a reference to the legend of Cain & Abel. Once people download and change C.A.I.N. to suit
their needs, it'll be the end of the existence of C.A.I.N., almost as though CAIN has been killed, and something new will
be born instead.
The 'C' in C.A.I.N. stands for "Collaborative" as CAIN by itself is not of much use. Only once somebody else collaborates
and modifies CAIN for their own use would it be useful. The 'N' stands for "Neuron" as C.A.I.N. will be the brain of the
A.I. that it is used in.
