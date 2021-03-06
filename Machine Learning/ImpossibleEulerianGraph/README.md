Introduction :
--------------
This is a project I had done as a part of my Design & Analysis of Algorithms Lab.

It involves traversing a graph from the start node and coming back to this start node, however, it does not follow
the condition for a Eulerian Graph where no path can be traversed more than once. The Algorithm used is covered in the
"Project Writeup.pdf" file.

In doing this, we can visit the same path-traversal pattern multiple times. As a result of this, this program is a
great way to feed training data into a Machine Learning algorithm.

Use Case Example :
------------------
For example, if we were to look at the shopping trends of a customer in an online shopping platform, if we take the items
bought by a customer to be the vertices of the graph, and the order in which items were bought to be the edges (we could
consider multiple items purchased together to all be connected to each other), we could feed training data into our
machine learning algorithm using the path found by this program.

Roles of Each File :
--------------------
This consists of a library file "Eulerian_Graph.py", which contains all the functions, class definitions and all the major
portions of the code, while the file "Impossible_Eulerian_Cycle.py" simple contains the driver code for a test case. The
"Impossible_Eulerian_Cycle.py" file should be edited to run your test cases.

Conclusion :
------------
I had a really good time exploring Graphs and coming up with the Algorithm for this task. I hope it can be of use to people
who are working on creating Machine Learning Libraries.

Thanks for having a look!

-- Shourojit
