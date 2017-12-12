#!/usr/bin/env python3
import sys
import os

"""This section of code exists only to allow
   the library file Eulerian_Graph.py to be used
   in this program."""

sys.path.append(os.getcwd())
import Eulerian_Graph

"""End of the aforementioned section of code."""


"""The driver code for the library classes and functions."""

Grph = Eulerian_Graph.Graph(4)
Grph.add_vertex("A", "B", "C", "D")
Grph.add_vertex("B", "A", "D")
Grph.add_vertex("C", "A", "D")
Grph.add_vertex("D", "A", "B", "C")

"""
The above code makes a graph like so :

    –––––––––– B –––––––––––
    |                       |
    A -–––––––––––––––––––– D
    |                       |
    –––––––––– C –––––––––––

"""

Grph.ImpossibleEulerCycle()
