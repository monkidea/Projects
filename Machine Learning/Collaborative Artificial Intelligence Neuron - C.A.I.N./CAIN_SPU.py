"""CAIN Semantics Processing Unit
Collaborative Artificial Intelligence Neuron v1.0"""

import numpy as np

# ========= Global Variables ==========
SEPERATORS = ['and', 'then', 'or', 'with']
"""Haven't used punctuation here, if you desire to you would put it here.
   It would look like:
   PUNCTUATION = list(",.?!-:;")
"""
VERBS = set()
PREPOSITIONS = set()
PRONOUNS = set()
textfile = open('verbs.txt', 'r').readlines()
for i in textfile:
    VERBS.add(i)
textfile = open('prepositions.txt', 'r').readlines()
for i in textfile:
    PREPOSITIONS.add(i)
textfile = open('pronouns.txt', 'r').readlines()
for i in textfile:
    PRONOUNS.add(i)
# ====== End of Global Variables ======


class CAIN_Sentence_Unit:
    """Sentence unit contains all the attributes of a sentence,
       i.e., subject, verb, object, preposition and faff."""

    def __init__(self, sentence):
        # Actual sentence that has been inputted.
        self.sentence = sentence
        # Now initializing the rest with value 'None'.
        self.sentence_object = None
        self.sentence_subject = None
        self.sentence_verb = None
        self.sentence_faff = None
        self.sentence_preposition = None


class CAIN_SPU:
    """Semantics Processing using classes as it is necessary
       to do so in order to properly process the data."""
    # Using Globals
    global SEPERATORS
    global VERBS
    global PREPOSITIONS
    global PRONOUNS

    def __init__(self, speech_to_text_output):
        # Taking the output from the Speech-to-Text unit as input
        self.stt_output = speech_to_text_output
        # Now calling Separation Engine. Each engine will in turn call the next
        CAIN_SPU.Separation_Engine(self.stt_output)

    def Separation_Engine(inp):
        # Separating the sentences.
        split_input = inp.split(" ")
        split_output = list()
        temp_buffer = ""
        for word in split_input:
            if word in SEPERATORS:
                split_output.append(temp_buffer[:-1])
                temp_buffer = ""
            else:
                temp_buffer += word + " "
        split_output.append(temp_buffer)
        # Creating CAIN Sentence Units out of split sentences.
        output_sentences = np.array(split_output)
        for i in range(len(output_sentences)):
            output_sentences[i] = CAIN_Sentence_Unit(output_sentences[i])
        """Now, feeding seperated sentences into structural analysis
           engine using a CAIN_Sentence_Unit object"""
        CAIN_SPU.Structural_Analysis_Engine(output_sentences)

    def StructAnalysis(CAIN_SU):
        """Here we check to find the verb in the sentence.
           In sentences, the subject directly precedes the verb in the sentence
           order and the object comes directly after the preposition.
           For example in the sentence,
           'He is walking to school', 'is' and 'walking' are verbs and 'He'
            directly precedes them. After the preposition, i.e. 'to', we get
            the word 'school' which is our object.
            As a foolproof method, we could use a set of pronouns to find
            the subject and use the verb-preceeding logic as a backup in case
            the subject for the sentence is not a pronoun.
            As for objects, the number of objects in the english language is
            far too great to be able to practically use it similar to the verbs
            so we can find the preposition and then choose the word that
            succeeds the preposition as the object. If we fail to do so, we can
            simply take the 2nd word after the verb as our object.
            """
        # First taking the sentence from the CSU and splitting it word-by-word.
        words_in_sentence = CAIN_SU.sentence.split(" ")
        verbs = list()
        obj = None
        subjects = list()
        prepositions = list()
        faff = list()

        for word in range(len(words_in_sentence)):  # For each word in sentence
            if words_in_sentence[word] in VERBS:
                verbs.append(words_in_sentence[word])
            elif words_in_sentence[word] in PRONOUNS:
                subjects.append(words_in_sentence[word])
            elif words_in_sentence[word] in PREPOSITIONS:
                prepositions.append(words_in_sentence[word])
                obj = words_in_sentence[word + 1]
            else:
                faff.append(words_in_sentence[word])

        """Now, just in case everything is not hunky dory at the end of this and
           we have special cases"""
        if len(subjects) == 0:  # If our pronoun matching did not work.
            subj_index = words_in_sentence.index(
                verbs[0]) - 1  # Index of subject is 1 before index of 1st verb
            subjects.append(words_in_sentence[subj_index])  # Add to subjects
            faff.remove(subjects[0])  # Removing the word from faff list.
        if obj is None:  # No object found.
            if(len(verbs) != 0):  # If sentence contains a verb.
                # Index of object is 2 after last verb
                obj_index = words_in_sentence.index(verbs[-1]) + 2
                obj = words_in_sentence[obj_index]
                faff.remove(obj)  # Removing the word from faff list.
            else:  # If sentence doesn't contain a verb.
                """This type of special case occurs with the sentence that
                   comes after a conjunction(any word in the SEPERATORS list),
                   in which the object directly succeeds the conjunction"""
                obj = words_in_sentence[0]

        return (verbs, obj, subjects, prepositions, faff)

    def Structural_Analysis_Engine(inp):
        """This Engine finds out the sentence structure. The heavy lifting here
           is actually done through the StructAnalysis() function. While that
           functionality could be implemented here itself, this was avoided for
           the sake of neatness and to have clean code. The actual methodology
           implemented to analyse the sentence is again mentioned in the body
           of the StructAnalysis function."""

        output = list()
        # Now, we have a list of CAIN_Sentence_Unit objects as input.
        for CSU in inp:  # CSU = CAIN Sentence Unit
            (CSU.sentence_verb, CSU.sentence_object,
             CSU.sentence_subject, CSU.sentence_preposition,
             CSU.sentence_faff) = CAIN_SPU.StructAnalysis(CSU)
            output.append(CSU)  # Adding processed CSU to output
        # Now, sending off the processed CSUs to the Faff Processing Engine.
        CAIN_SPU.Faff_Processing_Engine(output)

    def Faff_Processing_Engine(inp):
        """What we're doing here is simply removing the faff from the sentences
           and sending only the verb and object for Final Command Processing.
           If you would like to use the other attributes of the sentence, such
           as the subject or preposition in the Final_Command_Processing_Engine
           then feel free to send those as well.
           """
        # We're going to send a list of strings as output this time, not CSUs
        output_strings = list()
        # Now, we are receiving a list of CSUs as input.
        for CSU in inp:
            # Adjust the parameters to send to the FCPE here if needed.
            if(CSU.sentence_verb is not None):
                output_strings.append(
                    str(CSU.sentence_verb) + " " + str(CSU.sentence_object))
            else:  # In a special case where sentence has no verb.
                output_strings.append(str(CSU.sentence_object))
        # Now that that's all processed, sending output to Final Engine
        CAIN_SPU.Final_Command_Processing_Engine(output_strings)

    def Final_Command_Processing_Engine(inp):
        """The way in which the Command Processing Engine gives the output
           command will depend on the way that the user programmes it to. I am
           giving a simple output format of 'VERB_OBJECT' but you can feel free
           to change it to whatever you like. Some examples of changes could be
           'VERB@OBJECT'
           'OBJECT_VERB'
           'VERB->OBJECT' etc."""
        final_output_strings = list()
        for item in inp:
            temp_str_buffer = ""
            for character in item:
                # Here, all I'm doing is replacing the ' ' character with '_'
                if(character != ' '):
                    temp_str_buffer += character
                else:
                    temp_str_buffer += '_'
            # Now that string buffer has the desired value, adding it to output
            final_output_strings.append(temp_str_buffer)
        return final_output_strings
