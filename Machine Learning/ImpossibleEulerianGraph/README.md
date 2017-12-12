This is a project I had done as a part of my Design & Analysis of Algorithms Lab.

It involves traversing a graph from start node and coming back to this start node, however, it does not follow
the condition for a Eulerian Graph where no path can be traversed more than once.

In doing this, we can visit the same path-traversal pattern multiple times. As a result of this, this program is a
great way to feed training data into a Machine Learning algorithm.

For example, if we were to look at the shopping trends of a customer in an online shopping platform, if we take the items
bought by a customer to be the vertices of the graph, and the order in which items were bought to be the edges (we could
consider multiple items purchased together to all be connected to each other), we could feed training data into our
machine learning algorithm using the path found by this program.

This consists of a library file "Eulerian_Graph.py", which contains all the functions, class definitions and all the major
portions of the code, while the file "Impossible_Eulerian_Cycle.py" simple contains the driver code for a test case. The
"Impossible_Eulerian_Cycle.py" file should be edited to run your test cases.

Refer to the "Project Writeup.pdf" file for the algorithm I designed to accomplish this task.

Thanks for having a look!

- Shourojit
